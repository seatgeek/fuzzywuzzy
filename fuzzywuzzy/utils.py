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

def remove_punctuation(s):
    if s is None: return s
    s = s.replace(","," ").replace("."," ").replace("-"," ").replace(":"," ")
    return s

def validate_string(s):
    if s is None: return False
    try:
        if len(s) == 0: return False
    except:
        return False
    return True

def full_process(s):
    s = s.lower()
    s = s.strip()
    s = remove_punctuation(s)
    x = asciidammit(s)
    return x





