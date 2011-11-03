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


for s in cirque_strings:
    print 'Test for string: "%s"' % s
    print 'Old: %f' % round(timeit('utils.remove_punctuationold(\'%s\')' % s, "import utils",number=iterations),4)
    print 'New: %f' % round(timeit('utils.remove_punctuation(\'%s\')' % s, "import utils",number=iterations),4)
