from hypothesis import given, assume, settings
import hypothesis.strategies as st
import pytest
from itertools import product
from functools import partial

from fuzzywuzzy import fuzz, process, utils


def scorers_processors():
    scorers = [fuzz.ratio,
               fuzz.partial_ratio]
    processors = [lambda x: x,
                  partial(utils.full_process, force_ascii=False),
                  partial(utils.full_process, force_ascii=True)]
    splist = list(product(scorers, processors))
    splist.extend(
        [(fuzz.WRatio, partial(utils.full_process, force_ascii=True)),
         (fuzz.QRatio, partial(utils.full_process, force_ascii=True)),
         (fuzz.UWRatio, partial(utils.full_process, force_ascii=False)),
         (fuzz.UQRatio, partial(utils.full_process, force_ascii=False))]
    )

    return splist


@pytest.mark.parametrize('scorer,processor',
                         scorers_processors())
@given(data=st.data())
@settings(max_examples=100)
def test_random_strings_identical(scorer, processor, data):
    """
    Test that in a random set of identical strings, perfect matches
    :param scorer:
    :param processor:
    :param data:
    :return:
    """
    # Draw a list of random strings
    strings = data.draw(
        st.lists(st.text(min_size=10, max_size=100),
                 min_size=1, max_size=50))
    # Draw a random integer for the index in that list
    choiceidx = data.draw(st.integers(min_value=0, max_value=(len(strings) - 1)))
    choice = strings[choiceidx]

    if scorer in [fuzz.WRatio, fuzz.QRatio]:
        processor = partial(utils.full_process, force_ascii=True)
    elif scorer in [fuzz.UWRatio, fuzz.UQRatio]:
        processor = partial(utils.full_process, force_ascii=False)

    # Check process doesn't make our choice the empty string
    assume(processor(choice) != '')

    result = process.extractBests(choice,
                                  strings,
                                  scorer=scorer,
                                  processor=processor,
                                  score_cutoff=100,
                                  limit=None)

    # Check we get a result
    assert result != []

    # Check the result is in the list
    assert (choice, 100) in result
