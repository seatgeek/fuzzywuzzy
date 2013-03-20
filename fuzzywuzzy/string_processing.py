import re
import string
import unicodedata

class StringProcessor(object):
    """
    This class defines method to process strings in the most
    efficient way. Ideally all the methods below use unicode strings
    for both input and output.
    """

    MAX_UNICODE = 0x10ffff

    # For more information about unicode character categories,
    # check out: http://www.unicode.org/reports/tr44/tr44-4.html#General_Category_Values

    char_categories = "LMNPSZC"  # /L/etter /M/ark /N/umber /P/unctuation /S/ymbol /Z/eparator /C/ontrol
    char_family     = {}

    replace_separators_with_whitespace_regex = None
    chars_from_categories_regex = {}

    @classmethod
    def ensure_char_family_exists(cls, categories):
        """
        Build a dict of the form category: "characters in the category".
        The + [u"\\\\" if category == "P" else u""] part is needed because we need
        to escape backslash manually in the punctuation category.
        """

        for category in categories:
            if category not in cls.char_family and category in cls.char_categories:
                cls.char_family[category] = u"".join([unichr(i) for i in xrange(cls.MAX_UNICODE) if unicodedata.category(unichr(i))[0]==category] + \
                                                     [u"\\\\" if category == "P" else u""])

    @classmethod
    def ensure_chars_from_categories_regex_exists(cls, categories):
        """
        Build a dict of the form categories: regex_to_find_chars_from_categories.
        If categories is a set, a tuple, or a list, it is iterated over.
        Returns a unicode or a list of unicode depending on the input,
        where each unicode is a (sorted) key in cls.chars_from_categories_regex.
        """
        if isinstance(categories, set) or isinstance(categories, tuple) or isinstance(categories, list):
            sorted_cats = []
            needed_cats = set()
            for cats in categories:
                # Sort and check the existence of categories.
                sorted_cats.append(u"".join(sorted([cat for cat in cats if cat in cls.char_categories])))
                # Least common multiple approach.
                needed_cats = needed_cats.union(set([cat for cat in sorted_cats]))
            result = sorted_cats
        else:
            sorted_cats = [u"".join(sorted([cat for cat in categories if cat in cls.char_categories]))]
            needed_cats = set([cat for cat in sorted_cats])
            result = sorted_cats[0]

        # Make sure char_family is filled in with all that is needed.
        cls.ensure_char_family_exists(needed_cats)

        # Now make sure cls.chars_from_categories_regex is filled in with all that is needed.
        for sorted_cat in sorted_cats:
            if sorted_cat not in cls.chars_from_categories_regex:
                # Chars of interests.
                cls.chars_from_categories_regex[sorted_cat] = re.compile("[" + u"".join([cls.get_char_family(cat) for cat in sorted_cat]) + "]")

        return result

    @classmethod
    def get_char_family(cls, category):
        cls.ensure_char_family_exists(category)
        return cls.char_family[category]

    @classmethod
    def replace_separators_with_whitespace(cls, a_string):
        """
        This function replaces any sequence of separator (category Z) with a single white space.
        """
        # Chars of interests (possibly repeated).
        if not cls.replace_separators_with_whitespace_regex:
            cls.replace_separators_with_whitespace_regex = re.compile("[" + cls.get_char_family("Z") + "]+")
        return cls.replace_separators_with_whitespace_regex.sub(u" ", a_string)

    @classmethod
    def keep_only_chars_from_categories(cls, a_string, categories):
        """
        This function keeps only characters from categories it finds in the string given.
        """
        cat_key = cls.ensure_chars_from_categories_regex_exists(categories)
        return u"".join(cls.chars_from_categories_regex[cat_key].findall(a_string))

    @classmethod
    def strip_regex(cls, a_string, regex):
        """
        This function strips the regex in the string given.
        """

        return regex.sub(u"", a_string)

    @classmethod
    def strip(cls, a_string):
        """
        This function strips leading and trailing white space.
        """

        return a_string.strip()

    @classmethod
    def to_lower_case(cls, a_string):
        """
        This function returns the lower-cased version of the string given.
        """
        return a_string.lower()

    @classmethod
    def to_upper_case(cls, a_string):
        """
        This function returns the upper-cased version of the string given.
        """
        return a_string.upper()

