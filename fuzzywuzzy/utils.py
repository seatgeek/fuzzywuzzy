import string

table_pattern = ',.-:'
# Add chars whit ordinals over 127 to the table
for i in range(128, 256):
    table_pattern+=chr(i)
# translation table must have the same length
table_spaces = ' '*len(table_pattern)
punctuation_table = string.maketrans(table_pattern, table_spaces)

bad_chars=''
for i in range(128,256):
    bad_chars+=chr(i)

def asciionly(s):
    return s.translate(None, bad_chars)

# encode as string, decode as unicode bytes
'''
def asciidammitold(x):
    if type(x) is str:
        try:
            return x.decode('ascii')
        except:
            return x.decode('ascii', 'ignore')
    elif type(x) is unicode:
        try:
            return x.encode('ascii').decode('ascii')
        except:
            return x.encode('ascii', 'ignore').decode('ascii')
    else:
        return asciidammit(unicode(x))
'''

# remove non-ASCII characters from strings
def asciidammit(s):
    if type(s) is str:
        return asciionly(s)
    elif type(s) is unicode:
        return asciionly(s.encode('ascii', 'ignore'))
    else:
        return asciidammit(unicode(s))

def remove_punctuation(s):
    return string.translate(s, punctuation_table)

def validate_string(s):
    try:
        if len(s)>0:
            return True
        else:
            return False
    except:
        return False

def full_process(s):
    s = s.lower()
    s = s.strip()
    s = remove_punctuation(s)
    x = asciidammit(s)
    return x





