from fuzzywuzzy import fuzz
from difflib import SequenceMatcher

def matcher(s1, s2):
    """
    returns a SequenceMarcher
    """
    return SequenceMatcher(None, s1,s2)

def matchingblocks(s1, s2):
    """
    returns the blocks that matched
    """
    m = matcher(s1, s2)
    # FOR EACH BLOCK RETURN THE SUBSTRING THAT MATCHED
    # LEAVE OUT THE DUMMY ONE
    def sub(s, block):
        return s[block[0]:block[0]+block[2]] 
    
    return [sub(s1, block) for block in m.get_matching_blocks()[:-1]]

def largestmatchingblock(s1, s2):
    def matchsize(m):
        return m[2]
    m = matcher(s1, s2)
    return sorted(m.get_matching_blocks(), key=matchsize, reverse=True)[0]

def display(a, b):
    mbs = matchingblocks(a, b)
    if len(a)<=len(b):
        s, l = a, b
    else:
        s, l = b, a
    print "%s - %s" % (a,b)
    print "Matching blocks: %s" % ", ".join("'%s'" % mb for mb in mbs)
    largest_block = largestmatchingblock(s,l)
    l_start = largest_block[1]-largest_block[0]
    l_end = l_start+len(s)
    print "long_substr: %s" % l[l_start:l_end]
    print "Sum of matching chars: %s" % sum(len(mb) for mb in mbs)
    print "Length of the largest match: %s" % max(len(each) for each in mbs)
    print "Length of the shortest string: %s" % min(len(each) for each in (a,b))
    print "Result of partial_ratio: %s" % fuzz.partial_ratio(a, b)
    print

a="123 456 7890"
b="12 456"
c="456 90"

display(a, b)
display(a, c)

n="pedro daniel barreto rodrigues"
display("pedro rodrigues", n)
display("pedro daniel", n)
display("daniel rodrigues", n)
