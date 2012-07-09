# -*- coding: utf8 -*-

from timeit import timeit
from fuzzywuzzy import utils

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
    "Ça va?",
    "Cães danados",
    u"\xacCamarões assados",
    u"a\xac\u1234\u20ac\U00008000"
    ]


for s in choices:
    print 'Test for string: "%s"' % s
    # print 'Old: %f' % round(timeit('utils.validate_stringold(\'%s\')' % s, "from fuzzywuzzy import utils",number=iterations),4)
    print 'New: %f' % round(timeit('utils.validate_string(\'%s\')' % s, "from fuzzywuzzy import utils",number=iterations),4)

print

for s in mixed_strings:
    print 'Test for string: "%s"' % s
    #print 'Old: %f' % round(timeit('utils.asciidammitold(\'%s\')' % s, "from fuzzywuzzy import utils",number=iterations),4)
    print 'New: %f' % round(timeit('utils.asciidammit(\'%s\')' % s, "from fuzzywuzzy import utils",number=iterations),4)

print

for s in mixed_strings+cirque_strings+choices:
    print 'Test for string: "%s"' % s
    #print 'Old: %f' % round(timeit('utils.full_processold(\'%s\')' % s, "from fuzzywuzzy import utils",number=iterations),4)
    print 'New: %f' % round(timeit('utils.full_process(\'%s\')' % s, "from fuzzywuzzy import utils",number=iterations),4)

### benchmarking the core matching methods...

for s in cirque_strings:
    print 'Test fuzz.ratio for string: "%s"' % s
    print '-------------------------------'
    print 'New: %f' % round(timeit('fuzz.ratio(\'cirque du soleil\', \'%s\')' % s, "from fuzzywuzzy import fuzz",number=iterations/100),4)

for s in cirque_strings:
    print 'Test fuzz.partial_ratio for string: "%s"' % s
    print '-------------------------------'
    print 'New: %f' % round(timeit('fuzz.partial_ratio(\'cirque du soleil\', \'%s\')' % s, "from fuzzywuzzy import fuzz",number=iterations/100),4)

for s in cirque_strings:
    print 'Test fuzz.WRatio for string: "%s"' % s
    print '-------------------------------'
    print 'New: %f' % round(timeit('fuzz.WRatio(\'cirque du soleil\', \'%s\')' % s, "from fuzzywuzzy import fuzz",number=iterations/100),4)
