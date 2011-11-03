import string

# encode as string, decode as unicode bytes
def asciidammit(x):
    if type(x) is str:
        try:
            return x.decode('ascii')
        except:
            return x.decode('ascii', 'ignore')
    elif type(x) is unicode:
        try:
            s = x.encode('ascii')
            return s.decode('ascii')
        except:
            s = x.encode('ascii', 'ignore')
            return s.decode('ascii')
    else:
        x = unicode(x)
        return asciidammit(x)

def remove_punctuationold(s):
    if s is None: return s
    s = s.replace(","," ").replace("."," ").replace("-"," ").replace(":"," ")
    return s

table_pattern = ',.-:'
# Add chars whit ordinals over 127 to the table
for i in range(128, 256):
    table_pattern+=chr(i)
# translation table must have the same length
table_spaces = ' '*len(table_pattern)
punctuation_table = string.maketrans(table_pattern, table_spaces)

def remove_punctuation(s):
    return string.translate(s, punctuation_table)

def validate_stringold(s):
    if s is None: return False
    try:
        if len(s) == 0: return False
    except:
        return False
    return True

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





