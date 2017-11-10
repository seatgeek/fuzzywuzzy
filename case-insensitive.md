
* for ratio/partial_ratio, it is case sensitive
* but for token_sort_ratio/token_set_ratio is case insensitive

## would be better to make them consistent?

```
>>> fuzz.ratio("this is a test", "this is a test!")
97
>>> fuzz.ratio("this is a test", "this is a TEST!")
69
>>> fuzz.partial_ratio("this is a test", "this is a test!")
100
>>> fuzz.partial_ratio("this is a test", "this is a TEST!")
71
```
```
>>> fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
100
>>> fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a BEAR")
100
>>> fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
100
>>> fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a BEAR")
100
```
