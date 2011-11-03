from timeit import timeit
import utils

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


for s in cirque_strings:
    print 'Test for string: "%s"' % s
    print 'Old: %f' % round(timeit('utils.remove_punctuationold(\'%s\')' % s, "import utils",number=iterations),4)
    print 'New: %f' % round(timeit('utils.remove_punctuation(\'%s\')' % s, "import utils",number=iterations),4)

print

for s in choices:
    print 'Test for string: "%s"' % s
    print 'Old: %f' % round(timeit('utils.validate_stringold(\'%s\')' % s, "import utils",number=iterations*10),4)
    print 'New: %f' % round(timeit('utils.validate_string(\'%s\')' % s, "import utils",number=iterations*10),4)
