# -*- coding: utf8 -*-
from __future__ import unicode_literals
import unittest
import re
import sys
import pycodestyle

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from fuzzywuzzy import utils
from fuzzywuzzy.string_processing import StringProcessor

if sys.version_info[0] == 3:
    unicode = str

if sys.version_info[:2] == (2, 6):
    # Monkeypatch to make tests work on 2.6
    def assertLess(first, second, msg=None):
        assert first > second
    unittest.TestCase.assertLess = assertLess


class StringProcessingTest(unittest.TestCase):
    def test_replace_non_letters_non_numbers_with_whitespace(self):
        strings = ["new york mets - atlanta braves", "Cães danados",
                   "New York //// Mets $$$", "Ça va?"]
        for string in strings:
            proc_string = StringProcessor.replace_non_letters_non_numbers_with_whitespace(string)
            regex = re.compile(r"(?ui)[\W]")
            for expr in regex.finditer(proc_string):
                self.assertEqual(expr.group(), " ")

    def test_dont_condense_whitespace(self):
        s1 = "new york mets - atlanta braves"
        s2 = "new york mets atlanta braves"
        p1 = StringProcessor.replace_non_letters_non_numbers_with_whitespace(s1)
        p2 = StringProcessor.replace_non_letters_non_numbers_with_whitespace(s2)
        self.assertNotEqual(p1, p2)


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"
        self.mixed_strings = [
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
            "C'est la vie",
            "Ça va?",
            "Cães danados",
            "\xacCamarões assados",
            "a\xac\u1234\u20ac\U00008000",
            "\u00C1"
        ]

    def tearDown(self):
        pass

    def test_asciidammit(self):
        for s in self.mixed_strings:
            utils.asciidammit(s)

    def test_asciionly(self):
        for s in self.mixed_strings:
            # ascii only only runs on strings
            s = utils.asciidammit(s)
            utils.asciionly(s)

    def test_fullProcess(self):
        for s in self.mixed_strings:
            utils.full_process(s)

    def test_fullProcessForceAscii(self):
        for s in self.mixed_strings:
            utils.full_process(s, force_ascii=True)


class RatioTest(unittest.TestCase):

    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"
        self.s7 = 'new york city mets - atlanta braves'
        # test silly corner cases
        self.s8 = '{'
        self.s8a = '{'
        self.s9 = '{a'
        self.s9a = '{a'
        self.s10 = 'a{'
        self.s10a = '{b'

        self.cirque_strings = [
            "cirque du soleil - zarkana - las vegas",
            "cirque du soleil ",
            "cirque du soleil las vegas",
            "zarkana las vegas",
            "las vegas cirque du soleil at the bellagio",
            "zarakana - cirque du soleil - bellagio"
        ]

        self.baseball_strings = [
            "new york mets vs chicago cubs",
            "chicago cubs vs chicago white sox",
            "philladelphia phillies vs atlanta braves",
            "braves vs mets",
        ]

    def tearDown(self):
        pass

    def testEqual(self):
        self.assertEqual(fuzz.ratio(self.s1, self.s1a), 100)
        self.assertEqual(fuzz.ratio(self.s8, self.s8a), 100)
        self.assertEqual(fuzz.ratio(self.s9, self.s9a), 100)

    def testCaseInsensitive(self):
        self.assertNotEqual(fuzz.ratio(self.s1, self.s2), 100)
        self.assertEqual(fuzz.ratio(utils.full_process(self.s1), utils.full_process(self.s2)), 100)

    def testPartialRatio(self):
        self.assertEqual(fuzz.partial_ratio(self.s1, self.s3), 100)

    def testTokenSortRatio(self):
        self.assertEqual(fuzz.token_sort_ratio(self.s1, self.s1a), 100)

    def testPartialTokenSortRatio(self):
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s1, self.s1a), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s4, self.s5), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s8, self.s8a, full_process=False), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s9, self.s9a, full_process=True), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s9, self.s9a, full_process=False), 100)
        self.assertEqual(fuzz.partial_token_sort_ratio(self.s10, self.s10a, full_process=False), 50)

    def testTokenSetRatio(self):
        self.assertEqual(fuzz.token_set_ratio(self.s4, self.s5), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s8, self.s8a, full_process=False), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s9, self.s9a, full_process=True), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s9, self.s9a, full_process=False), 100)
        self.assertEqual(fuzz.token_set_ratio(self.s10, self.s10a, full_process=False), 50)

    def testPartialTokenSetRatio(self):
        self.assertEqual(fuzz.partial_token_set_ratio(self.s4, self.s7), 100)

    def testQuickRatioEqual(self):
        self.assertEqual(fuzz.QRatio(self.s1, self.s1a), 100)

    def testQuickRatioCaseInsensitive(self):
        self.assertEqual(fuzz.QRatio(self.s1, self.s2), 100)

    def testQuickRatioNotEqual(self):
        self.assertNotEqual(fuzz.QRatio(self.s1, self.s3), 100)

    def testWRatioEqual(self):
        self.assertEqual(fuzz.WRatio(self.s1, self.s1a), 100)

    def testWRatioCaseInsensitive(self):
        self.assertEqual(fuzz.WRatio(self.s1, self.s2), 100)

    def testWRatioPartialMatch(self):
        # a partial match is scaled by .9
        self.assertEqual(fuzz.WRatio(self.s1, self.s3), 90)

    def testWRatioMisorderedMatch(self):
        # misordered full matches are scaled by .95
        self.assertEqual(fuzz.WRatio(self.s4, self.s5), 95)

    def testWRatioUnicode(self):
        self.assertEqual(fuzz.WRatio(unicode(self.s1), unicode(self.s1a)), 100)

    def testQRatioUnicode(self):
        self.assertEqual(fuzz.WRatio(unicode(self.s1), unicode(self.s1a)), 100)

    def testEmptyStringsScore100(self):
        self.assertEqual(fuzz.ratio("", ""), 100)
        self.assertEqual(fuzz.partial_ratio("", ""), 100)

    def testIssueSeven(self):
        s1 = "HSINCHUANG"
        s2 = "SINJHUAN"
        s3 = "LSINJHUANG DISTRIC"
        s4 = "SINJHUANG DISTRICT"

        self.assertTrue(fuzz.partial_ratio(s1, s2) > 75)
        self.assertTrue(fuzz.partial_ratio(s1, s3) > 75)
        self.assertTrue(fuzz.partial_ratio(s1, s4) > 75)

    def testRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzz.ratio(s1, s2)
        self.assertEqual(0, score)

    def testPartialRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzz.partial_ratio(s1, s2)
        self.assertEqual(0, score)

    def testWRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzz.WRatio(s1, s2)
        self.assertEqual(0, score)

        # Cyrillic.
        s1 = "\u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433"
        s2 = "\u043f\u0441\u0438\u0445\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442"
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

        # Chinese.
        s1 = "\u6211\u4e86\u89e3\u6570\u5b66"
        s2 = "\u6211\u5b66\u6570\u5b66"
        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

    def testQRatioUnicodeString(self):
        s1 = "\u00C1"
        s2 = "ABCD"
        score = fuzz.QRatio(s1, s2)
        self.assertEqual(0, score)

        # Cyrillic.
        s1 = "\u043f\u0441\u0438\u0445\u043e\u043b\u043e\u0433"
        s2 = "\u043f\u0441\u0438\u0445\u043e\u0442\u0435\u0440\u0430\u043f\u0435\u0432\u0442"
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

        # Chinese.
        s1 = "\u6211\u4e86\u89e3\u6570\u5b66"
        s2 = "\u6211\u5b66\u6570\u5b66"
        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertNotEqual(0, score)

    def testQratioForceAscii(self):
        s1 = "ABCD\u00C1"
        s2 = "ABCD"

        score = fuzz.QRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzz.QRatio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testQRatioForceAscii(self):
        s1 = "ABCD\u00C1"
        s2 = "ABCD"

        score = fuzz.WRatio(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzz.WRatio(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testTokenSetForceAscii(self):
        s1 = "ABCD\u00C1 HELP\u00C1"
        s2 = "ABCD HELP"

        score = fuzz._token_set(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzz._token_set(s1, s2, force_ascii=False)
        self.assertLess(score, 100)

    def testTokenSortForceAscii(self):
        s1 = "ABCD\u00C1 HELP\u00C1"
        s2 = "ABCD HELP"

        score = fuzz._token_sort(s1, s2, force_ascii=True)
        self.assertEqual(score, 100)

        score = fuzz._token_sort(s1, s2, force_ascii=False)
        self.assertLess(score, 100)


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.testFunc = lambda *args, **kwargs: (args, kwargs)

    def testCheckForNone(self):
        invalid_input = [
            (None, None),
            ('Some', None),
            (None, 'Some')
        ]
        decorated_func = utils.check_for_none(self.testFunc)
        for i in invalid_input:
            self.assertEqual(decorated_func(*i), 0)

        valid_input = ('Some', 'Some')
        actual = decorated_func(*valid_input)
        self.assertNotEqual(actual, 0)

    def testCheckEmptyString(self):
        invalid_input = [
            ('', ''),
            ('Some', ''),
            ('', 'Some')
        ]
        decorated_func = utils.check_empty_string(self.testFunc)
        for i in invalid_input:
            self.assertEqual(decorated_func(*i), 0)

        valid_input = ('Some', 'Some')
        actual = decorated_func(*valid_input)
        self.assertNotEqual(actual, 0)


class ProcessTest(unittest.TestCase):

    def setUp(self):
        self.s1 = "new york mets"
        self.s1a = "new york mets"
        self.s2 = "new YORK mets"
        self.s3 = "the wonderful new york mets"
        self.s4 = "new york mets vs atlanta braves"
        self.s5 = "atlanta braves vs new york mets"
        self.s6 = "new york mets - atlanta braves"

        self.cirque_strings = [
            "cirque du soleil - zarkana - las vegas",
            "cirque du soleil ",
            "cirque du soleil las vegas",
            "zarkana las vegas",
            "las vegas cirque du soleil at the bellagio",
            "zarakana - cirque du soleil - bellagio"
        ]

        self.baseball_strings = [
            "new york mets vs chicago cubs",
            "chicago cubs vs chicago white sox",
            "philladelphia phillies vs atlanta braves",
            "braves vs mets",
        ]

    def testGetBestChoice1(self):
        query = "new york mets at atlanta braves"
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], "braves vs mets")

    def testGetBestChoice2(self):
        query = "philadelphia phillies at atlanta braves"
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[2])

    def testGetBestChoice3(self):
        query = "atlanta braves at philadelphia phillies"
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[2])

    def testGetBestChoice4(self):
        query = "chicago cubs vs new york mets"
        best = process.extractOne(query, self.baseball_strings)
        self.assertEqual(best[0], self.baseball_strings[0])

    def testWithProcessor(self):
        events = [
            ["chicago cubs vs new york mets", "CitiField", "2011-05-11", "8pm"],
            ["new york yankees vs boston red sox", "Fenway Park", "2011-05-11", "8pm"],
            ["atlanta braves vs pittsburgh pirates", "PNC Park", "2011-05-11", "8pm"],
        ]
        query = ["new york mets vs chicago cubs", "CitiField", "2017-03-19", "8pm"],

        best = process.extractOne(query, events, processor=lambda event: event[0])
        self.assertEqual(best[0], events[0])

    def testWithScorer(self):
        choices = [
            "new york mets vs chicago cubs",
            "chicago cubs at new york mets",
            "atlanta braves vs pittsbugh pirates",
            "new york yankees vs boston red sox"
        ]

        choices_dict = {
            1: "new york mets vs chicago cubs",
            2: "chicago cubs vs chicago white sox",
            3: "philladelphia phillies vs atlanta braves",
            4: "braves vs mets"
        }

        # in this hypothetical example we care about ordering, so we use quick ratio
        query = "new york mets at chicago cubs"
        scorer = fuzz.QRatio

        # first, as an example, the normal way would select the "more
        # 'complete' match of choices[1]"

        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

        # now, use the custom scorer

        best = process.extractOne(query, choices, scorer=scorer)
        self.assertEqual(best[0], choices[0])

        best = process.extractOne(query, choices_dict)
        self.assertEqual(best[0], choices_dict[1])

    def testWithCutoff(self):
        choices = [
            "new york mets vs chicago cubs",
            "chicago cubs at new york mets",
            "atlanta braves vs pittsbugh pirates",
            "new york yankees vs boston red sox"
        ]

        query = "los angeles dodgers vs san francisco giants"

        # in this situation, this is an event that does not exist in the list
        # we don't want to randomly match to something, so we use a reasonable cutoff

        best = process.extractOne(query, choices, score_cutoff=50)
        self.assertTrue(best is None)
        # self.assertIsNone(best) # unittest.TestCase did not have assertIsNone until Python 2.7

        # however if we had no cutoff, something would get returned

        # best = process.extractOne(query, choices)
        # self.assertIsNotNone(best)

    def testWithCutoff2(self):
        choices = [
            "new york mets vs chicago cubs",
            "chicago cubs at new york mets",
            "atlanta braves vs pittsbugh pirates",
            "new york yankees vs boston red sox"
        ]

        query = "new york mets vs chicago cubs"
        # Only find 100-score cases
        res = process.extractOne(query, choices, score_cutoff=100)
        self.assertTrue(res is not None)
        best_match, score = res
        self.assertTrue(best_match is choices[0])

    def testEmptyStrings(self):
        choices = [
            "",
            "new york mets vs chicago cubs",
            "new york yankees vs boston red sox",
            "",
            ""
        ]

        query = "new york mets at chicago cubs"

        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

    def testNullStrings(self):
        choices = [
            None,
            "new york mets vs chicago cubs",
            "new york yankees vs boston red sox",
            None,
            None
        ]

        query = "new york mets at chicago cubs"

        best = process.extractOne(query, choices)
        self.assertEqual(best[0], choices[1])

    def test_list_like_extract(self):
        """We should be able to use a list-like object for choices."""
        def generate_choices():
            choices = ['a', 'Bb', 'CcC']
            for choice in choices:
                yield choice
        search = 'aaa'
        result = [(value, confidence) for value, confidence in
                  process.extract(search, generate_choices())]
        self.assertTrue(len(result) > 0)

    def test_dict_like_extract(self):
        """We should be able to use a dict-like object for choices, not only a
        dict, and still get dict-like output.
        """
        try:
            from UserDict import UserDict
        except ImportError:
            from collections import UserDict
        choices = UserDict({'aa': 'bb', 'a1': None})
        search = 'aaa'
        result = process.extract(search, choices)
        self.assertTrue(len(result) > 0)
        for value, confidence, key in result:
            self.assertTrue(value in choices.values())

    def test_dedupe(self):
        """We should be able to use a list-like object for contains_dupes
        """
        # Test 1
        contains_dupes = ['Frodo Baggins', 'Tom Sawyer', 'Bilbo Baggin', 'Samuel L. Jackson', 'F. Baggins', 'Frody Baggins', 'Bilbo Baggins']

        result = process.dedupe(contains_dupes)
        self.assertTrue(len(result) < len(contains_dupes))

        # Test 2
        contains_dupes = ['Tom', 'Dick', 'Harry']

        # we should end up with the same list since no duplicates are contained in the list (e.g. original list is returned)
        deduped_list = ['Tom', 'Dick', 'Harry']

        result = process.dedupe(contains_dupes)
        self.assertEqual(result, deduped_list)

    def test_simplematch(self):
        basic_string = 'a, b'
        match_strings = ['a, b']

        result = process.extractOne(basic_string, match_strings, scorer=fuzz.ratio)
        part_result = process.extractOne(basic_string, match_strings, scorer=fuzz.partial_ratio)

        self.assertEqual(result, ('a, b', 100))
        self.assertEqual(part_result, ('a, b', 100))


class TestCodeFormat(unittest.TestCase):
    def test_pep8_conformance(self):
        pep8style = pycodestyle.StyleGuide(quiet=False)
        pep8style.options.ignore = pep8style.options.ignore + tuple(['E501'])
        pep8style.input_dir('fuzzywuzzy')
        result = pep8style.check_files()
        self.assertEqual(result.total_errors, 0, "PEP8 POLICE - WOOOOOWOOOOOOOOOO")

if __name__ == '__main__':
    unittest.main()         # run all tests
