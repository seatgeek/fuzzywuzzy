import string

bad_chars=''
for i in range(128,256):
    bad_chars+=chr(i)
table_from=string.punctuation+string.ascii_uppercase
table_to=' '*len(string.punctuation)+string.ascii_lowercase
trans_table=string.maketrans(table_from, table_to)


def asciionly(s):
    return s.translate(None, bad_chars)

# remove non-ASCII characters from strings
def asciidammit(s):
    if type(s) is str:
        return asciionly(s)
    elif type(s) is unicode:
        return asciionly(s.encode('ascii', 'ignore'))
    else:
        return asciidammit(unicode(s))

def validate_string(s):
    try:
        if len(s)>0:
            return True
        else:
            return False
    except:
        return False

def full_process(s):
    s = asciidammit(s)
    return s.translate(trans_table, bad_chars).strip()

def intr(n):
    '''Returns a correctly rounded integer'''
    return int(round(n))


