from functools import partial

from hypothesis import given, assume, settings
import hypothesis.strategies as st
import pytest

from fuzzywuzzy import fuzz, process, utils


def scorers():
    """
    Generate a list of scorers for testing

    :return: [scorer,...]
    """
    scorerslist = [fuzz.ratio,
                   fuzz.partial_ratio,
                   fuzz.WRatio,
                   fuzz.QRatio,
                   fuzz.UWRatio,
                   fuzz.UQRatio,
                   fuzz.token_set_ratio,
                   fuzz.token_sort_ratio,
                   fuzz.partial_token_set_ratio,
                   fuzz.partial_token_sort_ratio
                  ]
    return scorerslist


def full_scorers():
    """
    Generate a list of scores for testing that use the full string only

    :return: [scorer,...]
    """
    scorerslist = [fuzz.ratio,
                   fuzz.WRatio,
                   fuzz.QRatio,
                   fuzz.UWRatio,
                   fuzz.UQRatio
                  ]
#    processors = [lambda x: x,
#                  partial(utils.full_process, force_ascii=False),
#                  partial(utils.full_process, force_ascii=True)]
#    splist = list(product(scorers, processors))
#    splist.extend(
#        [(fuzz.WRatio, partial(utils.full_process, force_ascii=True)),
#         (fuzz.QRatio, partial(utils.full_process, force_ascii=True)),
#         (fuzz.UWRatio, partial(utils.full_process, force_ascii=False)),
#         (fuzz.UQRatio, partial(utils.full_process, force_ascii=False))]
#    )

    return scorerslist


@pytest.mark.parametrize('scorer',
                         scorers())
@given(data=st.data())
@settings(max_examples=100)
def test_identical_strings_extracted(scorer, data):
    """
    Test that identical strings will always return a perfect match.

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

    # Extract our choice from the list
    choice = strings[choiceidx]

    # Check scorer doesn't make our choice the empty string
    empty_check_function = partial(utils.full_process, force_ascii=True)
    # If the scorer doesnt performs full_ratio with force ascii then don't use force_ascii to check blanks
    if scorer not in [fuzz.WRatio, fuzz.QRatio,
                      fuzz.token_set_ratio, fuzz.token_sort_ratio,
                      fuzz.partial_token_set_ratio, fuzz.partial_token_sort_ratio]:
        empty_check_function = partial(utils.full_process, force_ascii=False)
    assume(empty_check_function(choice) != '')

    # Extract all perfect matches
    result = process.extractBests(choice,
                                  strings,
                                  scorer=scorer,
                                  processor=None,
                                  score_cutoff=100,
                                  limit=None)

    # Check we get a result
    assert result != []

    # Check the original is in the list
    assert (choice, 100) in result


@pytest.mark.parametrize('scorer',
                         full_scorers())
@given(data=st.data())
@settings(max_examples=100)
def test_only_identical_strings_extracted(scorer, data):
    """
    Test that only identical (post processing) strings score 100 on the test.

    If two strings are not identical then using full comparison methods they should
    not be a perfect (100) match.

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

    # Extract our choice from the list
    choice = strings[choiceidx]

    # Check scorer doesn't make our choice the empty string
    empty_check_function = partial(utils.full_process, force_ascii=True)
    # If the scorer doesnt performs full_ratio with force ascii then don't use force_ascii to check blanks
    if scorer not in [fuzz.WRatio, fuzz.QRatio,
                      fuzz.token_set_ratio, fuzz.token_sort_ratio,
                      fuzz.partial_token_set_ratio, fuzz.partial_token_sort_ratio]:
        empty_check_function = partial(utils.full_process, force_ascii=False)
    assume(empty_check_function(choice) != '')

    # Extract all perfect matches
    result = process.extractBests(choice,
                                  strings,
                                  scorer=scorer,
                                  processor=None,
                                  score_cutoff=100,
                                  limit=None)

    # Check we get a result
    assert result != []

    # Check THE ONLY result(s) we get are a perfect match for the (processed) original data
    for r in result:
        assert choice == r[0]
