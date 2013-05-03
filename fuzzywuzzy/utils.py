from string_processing import StringProcessor

def validate_string(s):
    try:
        if len(s)>0:
            return True
        else:
            return False
    except:
        return False

bad_chars=''
for i in range(128,256):
    bad_chars+=chr(i)

def asciionly(s):
    return s.translate(None, bad_chars)

def asciidammit(s):
    if type(s) is str:
        return asciionly(s)
    elif type(s) is unicode:
        return asciionly(s.encode('ascii', 'ignore'))
    else:
        return asciidammit(unicode(s))

def full_process(s, force_ascii=False):
    """Process string by
        -- removing all but letters and numbers
        -- trim whitespace
        -- force to lower case
        if force_ascii == True, force convert to ascii"""

    if s is None:
        return u""

    if force_ascii:
        s = asciidammit(s)
    # Keep only Letters and Numbres (see Unicode docs).
    string_out = StringProcessor.replace_non_lettters_non_numbers_with_whitespace(s)
    # Force into lowercase.
    string_out = StringProcessor.to_lower_case(string_out)
    # Remove leading and trailing whitespaces.
    string_out = StringProcessor.strip(string_out)
    return string_out

def intr(n):
    '''Returns a correctly rounded integer'''
    return int(round(n))
