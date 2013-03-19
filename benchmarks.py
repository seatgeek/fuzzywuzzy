# -*- coding: utf8 -*-

from timeit import timeit
from fuzzywuzzy import utils
import math

iterations=100000

cirque_strings = [
    "cirque du soleil - zarkana - las vegas",
    "cirque du soleil ",
    "cirque du soleil las vegas",
    "zarkana las vegas",
    "las vegas cirque du soleil at the bellagio",
    "zarakana - cirque du soleil - bellagio"
    ]

choices = [
    "",
    "new york yankees vs boston red sox",
    "",
    "zarakana - cirque du soleil - bellagio",
    None,
    "cirque du soleil las vegas",
    None
]

mixed_strings = [
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    "C\\'est la vie",
    u"Ça va?",
    u"Cães danados",
    u"\xacCamarões assados",
    u"a\xac\u1234\u20ac\U00008000"
    ]

def print_result_from_timeit(stmt='pass', setup='pass', number=1000000):
    """
    Clean function to know how much time took the execution of one statement
    """
    units     = ["s", "ms", "us", "ns"]
    thousands = int(math.log(number, 1000))

    print "Average took %f %s" % (round(timeit(stmt, setup, number=number),4) * (1000**thousands) / number, units[thousands])

for s in choices:
    print 'Test validate_string for: "%s"' % s
    print_result_from_timeit('utils.validate_string(\'%s\')' % s, "from fuzzywuzzy import utils", number=iterations)

print

for s in mixed_strings+cirque_strings+choices:
    print 'Test full_process for: "%s"' % s
    print_result_from_timeit('utils.full_process(u\'%s\')' % s, "from fuzzywuzzy import utils",number=iterations)

### benchmarking the core matching methods...

for s in cirque_strings:
    print 'Test fuzz.ratio for string: "%s"' % s
    print '-------------------------------'
    print_result_from_timeit('fuzz.ratio(u\'cirque du soleil\', u\'%s\')' % s, "from fuzzywuzzy import fuzz",number=iterations/100)

for s in cirque_strings:
    print 'Test fuzz.partial_ratio for string: "%s"' % s
    print '-------------------------------'
    print_result_from_timeit('fuzz.partial_ratio(u\'cirque du soleil\', u\'%s\')' % s, "from fuzzywuzzy import fuzz",number=iterations/100)

for s in cirque_strings:
    print 'Test fuzz.WRatio for string: "%s"' % s
    print '-------------------------------'
    print_result_from_timeit('fuzz.WRatio(u\'cirque du soleil\', u\'%s\')' % s, "from fuzzywuzzy import fuzz",number=iterations/100)
