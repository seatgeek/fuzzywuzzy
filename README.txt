INSTALLATION INSTRUCTIONS

1) Download tarball or clone git repository
2) run python setup.py install

USING FUZZYWUZZY (examples)

> from fuzzywuzzy import fuzz
> from fuzzywuzzy import process

# SIMPLE RATIO
> fuzz.ratio("this is a test", "this is a test!")
96

# PARTIAL RATIO
> fuzz.partial_ratio("this is a test", "this is a test!")
100

# TOKEN SET RATIO
> fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
90
> fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
100

# TOKEN SET RATIO
> fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
84
> fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
100



