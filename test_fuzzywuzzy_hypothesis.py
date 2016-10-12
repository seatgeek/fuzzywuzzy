import unittest
from hypothesis import given, assume, settings
import hypothesis.strategies as st

from fuzzywuzzy import fuzz, process, utils


class ProcessHypothesisTests(unittest.TestCase):

    @given(st.data())
    @settings(max_examples=100)
    def test_random_strings_processed(self, data):
        # Draw a list of random strings
        strings = data.draw(
            st.lists(st.text(min_size=10, max_size=100),
                     min_size=1, max_size=50))
        # Draw a random integer for the index in that list
        choiceidx = data.draw(st.integers(min_value=0, max_value=(len(strings) - 1)))
        choice = strings[choiceidx]

        # Check full process doesn't make our choice the empty string
        assume(utils.full_process(choice) != '')

        result = process.extractOne(choice, strings, scorer=fuzz.ratio, processor=utils.full_process)

        # Check we get a result
        self.assertIsNotNone(result)

        # Check the result is a perfect match according to fuzz.ratio
        self.assertEqual(result[1], 100)

        # Assert the results are equal after processing
        self.assertEqual(utils.full_process(choice),
                         utils.full_process(result[0]))

    @given(st.data())
    @settings(max_examples=100)
    def test_random_strings_unprocessed(self, data):
        # Draw a list of random strings
        strings = data.draw(
            st.lists(st.text(min_size=10, max_size=100),
                     min_size=1, max_size=50))
        # Draw a random integer for the index in that list
        choiceidx = data.draw(st.integers(min_value=0, max_value=(len(strings) - 1)))
        choice = strings[choiceidx]

        result = process.extractOne(choice, strings,
                                    scorer=fuzz.ratio,
                                    processor=lambda x: x)

        # Check we get a result
        self.assertIsNotNone(result)

        # Check the result is a perfect match according to fuzz.ratio
        self.assertEqual(result[1], 100)

        # Assert the results are equal after processing
        self.assertEqual(choice,
                         result[0])
