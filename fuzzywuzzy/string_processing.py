import re
import string
import unicodedata

class StringProcessor(object):
    """
    This class defines method to process strings in the most
    efficient way. Ideally all the methods below use unicode strings
    for both input and output.
    """

    # For more information about unicode character categories,
    # check out: http://www.unicode.org/reports/tr44/tr44-4.html#General_Category_Values
    all_chars       = None

    char_categories = "LMNPSZC" # /L/etter /M/ark /N/umber /P/unctuation /S/ymbol /Z/eparator /C/ontrol
    char_family     = {}

    replace_separators_with_whitespace_regex = None
    chars_from_categories_regex = {}
    words_from_categories_regex = {}

    @classmethod
    def get_all_chars(cls):
        if not cls.all_chars:
            cls.all_chars = u"".join(unichr(i) for i in xrange(0x10ffff))
        return cls.all_chars

    @classmethod
    def get_char_family(cls, category):
        if not category in cls.char_family:
            # Build a dict of the form category: "characters in the category".
            # The + [u"\\\\" if category == "P" else u""] part is needed because we need
            # to escape backslash manually in the punctuation category.
            cls.char_family[category] = u"".join([char for char in cls.get_all_chars() if unicodedata.category(char)[0]==category] + \
                                                 [u"\\\\" if category == "P" else u""])
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
    def strip_chars_from_categories(cls, a_string, categories):
        """
        This function strips characters from categories down in the string given.
        """
        if not categories in cls.chars_from_categories_regex:
            # Chars of interests.
            cls.chars_from_categories_regex[categories] = \
                re.compile("[" + u"".join([cls.get_char_family(category) for category in categories]) + "]")

        return cls.chars_from_categories_regex[categories].sub(u"", a_string)

    @classmethod
    def keep_only_chars_from_categories(cls, a_string, categories):
        """
        This function keeps only characters from categories it finds in the string given.
        """
        if not categories in cls.chars_from_categories_regex:
            # Chars of interests.
            cls.chars_from_categories_regex[categories] = \
                re.compile("[" + u"".join([cls.get_char_family(category) for category in categories]) + "]")

        return u"".join(cls.chars_from_categories_regex[categories].findall(a_string))


    @classmethod
    def strip_words_from_categories(cls, a_string, categories):
        """
        This function strips words whose characters belong to categories in the string given.
        """
        if not categories in cls.words_from_categories_regex:
            # Separator or start of string + Chars of interests (possibly repeated) + Separator or end of string.
            cls.words_from_categories_regex[categories] = \
                re.compile("((?<=[" + cls.get_char_family("Z") +"])|^)" + \
                           "[" + u"".join([cls.get_char_family(category) for category in categories]) + "]+" + \
                           "((?=[" + cls.get_char_family("Z") + "])|$)")

        return cls.words_from_categories_regex[categories].sub(u"", a_string)

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

