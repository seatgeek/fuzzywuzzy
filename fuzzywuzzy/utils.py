from string_processing import StringProcessor

# asciidammit prevents any proper unicode processing
# and would return u"None" when fed with None.
#
# import string
#
# bad_chars=''
# for i in range(128,256):
#     bad_chars+=chr(i)
# table_from=string.punctuation+string.ascii_uppercase
# table_to=' '*len(string.punctuation)+string.ascii_lowercase
# trans_table=string.maketrans(table_from, table_to)
#
#
# def asciionly(s):
#     return s.translate(None, bad_chars)
#
#  remove non-ASCII characters from strings
# def asciidammit(s):
#     if type(s) is str:
#         return asciionly(s)
#     elif type(s) is unicode:
#         return asciionly(s.encode('ascii', 'ignore'))
#     else:
#         return asciidammit(unicode(s))

def validate_string(s):
    try:
        if len(s)>0:
            return True
        else:
            return False
    except:
        return False

def full_process(s):
    if s is None:
        return u""
    string_out = StringProcessor.keep_only_chars_from_categories(s, "LNZ")      # Keep only Letters Numbers and Zeparators.
    string_out = StringProcessor.to_lower_case(string_out)                      # Force into lowercase.
    string_out = StringProcessor.replace_separators_with_whitespace(string_out) # Convert zeparators into whitespaces.
    string_out = StringProcessor.strip(string_out)                              # Remove leading and trailing whitespaces.
    return string_out

def intr(n):
    '''Returns a correctly rounded integer'''
    return int(round(n))


