import re
import string


class StringProcessor(object):
    """
    This class defines method to process strings in the most
    efficient way. Ideally all the methods below use unicode strings
    for both input and output.
    """

    regex = re.compile(r"(?ui)\W")

    @classmethod
    def replace_non_lettters_non_numbers_with_whitespace(cls, a_string):
        """
        This function replaces any sequence of non letters and non numbers with a single white space.
        """
        return cls.regex.sub(u" ", a_string)

    strip = staticmethod(string.strip)
    to_lower_case = staticmethod(string.lower)
    to_upper_case = staticmethod(string.upper)
