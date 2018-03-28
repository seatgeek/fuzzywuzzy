#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
import platform
import warnings

try:
    from .StringMatcher import StringMatcher as SequenceMatcher
except ImportError:
    if platform.python_implementation() != "PyPy":
        warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
    from difflib import SequenceMatcher

from fuzzywuzzymit import fuzz as _fuzz
from fuzzywuzzymit.fuzz import *

_fuzz.SequenceMatcher = SequenceMatcher
del _fuzz
