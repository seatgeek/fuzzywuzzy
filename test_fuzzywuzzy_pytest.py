import warnings
from fuzzywuzzy import process


def test_process_warning():
    """Check that a string reduced to 0 by processor raises a warning"""
    query = ':::::::'
    choices = [':::::::']
    with warnings.catch_warnings(record=True) as w:
        result = process.extractOne(query, choices)
        assert issubclass(w[-1].category, UserWarning)
        assert result == (query, 0)
