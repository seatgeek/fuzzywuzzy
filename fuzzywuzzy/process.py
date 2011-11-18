#!/usr/bin/env python
# encoding: utf-8
"""
process.py

Copyright (c) 2011 Adam Cohen

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from fuzz import *

import sys, os
import utils

#######################################
# Find Best Matchs In List Of Choices #
#######################################

def extract(query, choices, processor=None, scorer=None, limit=5):

    # choices       = a list of objects we are attempting to extract values from
    # query         = an object representing the thing we want to find
    # scorer        f(OBJ, QUERY) --> INT. We will return the objects with the highest score
        # by default, we use score.WRatio() and both OBJ and QUERY should be strings
    # processor     f(OBJ_A) --> OBJ_B, where the output is an input to scorer
        # for example, "processor = lambda x: x[0]" would return the first element in a collection x (of, say, strings)
        # this would then be used in the scoring collection

    if choices is None or len(choices) == 0:
        return []

    # default, turn whatever the choice is into a string
    if processor is None:
        processor = lambda x: utils.asciidammit(x)

    # default: wratio
    if scorer is None:
        scorer = WRatio

    sl = list()

    for choice in choices:
        processed = processor(choice)
        score = scorer(query, processed)
        tuple = (choice, score)
        sl.append(tuple)

    sl.sort(key=lambda i: -1*i[1])
    return sl[:limit]

##########################
# Find Single Best Match #
##########################

def extractOne(query, choices, processor=None, scorer=None, score_cutoff=0):

    # convenience method which returns the single best choice
    # optional parameter: score_cutoff.
        # If the best choice has a score of less than score_cutoff
        # we will return none (intuition: not a good enough match)

    best_list = extract(query, choices, processor, scorer, limit=1)
    if len(best_list) > 0:
        best = best_list[0]
        if best[1] > score_cutoff:
            return best
        else:
            return None
    else:
        return None
