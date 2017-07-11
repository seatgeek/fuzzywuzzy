# -*- coding: utf8 -*-

from timeit import timeit
import math
import csv

iterations = 100000


reader = csv.DictReader(open('data/titledata.csv'), delimiter='|')
titles = [i['custom_title'] for i in reader]
title_blob = '\n'.join(titles)


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

common_setup = "from fuzzywuzzy import fuzz, utils; "
basic_setup = "from fuzzywuzzy.string_processing import StringProcessor;"


def print_result_from_timeit(stmt='pass', setup='pass', number=1000000):
    """
    Clean function to know how much time took the execution of one statement
    """
    units = ["s", "ms", "us", "ns"]
    duration = timeit(stmt, setup, number=number)
    avg_duration = duration / float(number)
    thousands = int(math.floor(math.log(avg_duration, 1000)))

    print "Total time: %fs. Average run: %.3f%s." \
        % (duration, avg_duration * (1000 ** -thousands), units[-thousands])

for s in choices:
    print 'Test validate_string for: "%s"' % s
    print_result_from_timeit('utils.validate_string(\'%s\')' % s, common_setup, number=iterations)

print

for s in mixed_strings + cirque_strings + choices:
    print 'Test full_process for: "%s"' % s
    print_result_from_timeit('utils.full_process(u\'%s\')' % s,
                             common_setup + basic_setup, number=iterations)

# benchmarking the core matching methods...

for s in cirque_strings:
    print 'Test fuzz.ratio for string: "%s"' % s
    print '-------------------------------'
    print_result_from_timeit('fuzz.ratio(u\'cirque du soleil\', u\'%s\')' % s,
                             common_setup + basic_setup, number=iterations / 100)

for s in cirque_strings:
    print 'Test fuzz.partial_ratio for string: "%s"' % s
    print '-------------------------------'
    print_result_from_timeit('fuzz.partial_ratio(u\'cirque du soleil\', u\'%s\')'
                             % s, common_setup + basic_setup, number=iterations / 100)

for s in cirque_strings:
    print 'Test fuzz.WRatio for string: "%s"' % s
    print '-------------------------------'
    print_result_from_timeit('fuzz.WRatio(u\'cirque du soleil\', u\'%s\')' % s,
                             common_setup + basic_setup, number=iterations / 100)
                             

print 'Test process.exract(scorer =  fuzz.QRatio) for string: "%s"' % s
print '-------------------------------'
print_result_from_timeit('process.extract(u\'cirque du soleil\', choices, scorer =  fuzz.QRatio)',
                             common_setup + basic_setup + " from fuzzywuzzy import process; import string,random; random.seed(18);"
                             " choices = [\'\'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30)) for s in range(5000)]",
                              number=10)

print 'Test process.exract(scorer =  fuzz.WRatio) for string: "%s"' % s
print '-------------------------------'
print_result_from_timeit('process.extract(u\'cirque du soleil\', choices, scorer =  fuzz.WRatio)',
                             common_setup + basic_setup + " from fuzzywuzzy import process; import string,random; random.seed(18);"
                             " choices = [\'\'.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30)) for s in range(5000)]",
                              number=10)


# let me show you something

s = 'New York Yankees'

test = 'import functools\n'
test += 'title_blob = """%s"""\n' % title_blob
test += 'title_blob = title_blob.strip()\n'
test += 'titles = title_blob.split("\\n")\n'

print 'Real world ratio(): "%s"' % s
print '-------------------------------'
test += 'prepared_ratio = functools.partial(fuzz.ratio, "%s")\n' % s
test += 'titles.sort(key=prepared_ratio)\n'
print_result_from_timeit(test,
                         common_setup + basic_setup,
                         number=100)
