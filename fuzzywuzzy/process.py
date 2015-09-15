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
import itertools

from . import fuzz
from . import utils


def extract(query, choices, processor=None, scorer=None, limit=5):
    """Select the best match in a list or dictionary of choices.

    Find best matches in a list or dictionary of choices, return a
    list of tuples containing the match and it's score. If a dictionary
    is used, also returns the key for each match.

    Arguments:
        query: An object representing the thing we want to find.
        choices: An iterable or dictionary-like object containing choices
            to be matched against the query. Dictionary arguments of
            {key: value} pairs will attempt to match the query against
            each value.
        processor: Optional function of the form f(a) -> b, where a is an
            individual choice and b is the choice to be used in matching.

            This can be used to match against, say, the first element of
            a list:

            lambda x: x[0]

            Defaults to fuzzywuzzy.utils.full_process().
        scorer: Optional function for scoring matches between the query and
            an individual processed choice. This should be a function
            of the form f(query, choice) -> int.

            By default, fuzz.WRatio() is used and expects both query and
            choice to be strings.
        limit: Optional maximum for the number of elements returned. Defaults
            to 5.

    Returns:
        List of tuples containing the match and its score.

        If a list is used for choices, then the result will be 2-tuples.
        If a dictionary is used, then the result will be 3-tuples containing
        he key for each match.

        For example, searching for 'bird' in the dictionary

        {'bard': 'train', 'dog': 'man'}

        may return

        [('train', 22, 'bard'), ('man', 0, 'dog')]
    """

    if choices is None:
        return []

    # Catch generators without lengths
    try:
        if len(choices) == 0:
            return []
    except TypeError:
        pass

    # default, turn whatever the choice is into a workable string
    if not processor:
        processor = utils.full_process

    # default: wratio
    if not scorer:
        scorer = fuzz.WRatio

    sl = []

    try:
        # See if choices is a dictionary-like object.
        for key, choice in choices.items():
            processed = processor(choice)
            score = scorer(query, processed)
            sl.append((choice, score, key))
    except AttributeError:
        # It's a list; just iterate over it.
        for choice in choices:
            processed = processor(choice)
            score = scorer(query, processed)
            sl.append((choice, score))

    sl.sort(key=lambda i: i[1], reverse=True)
    return sl[:limit]


def extractBests(query, choices, processor=None, scorer=None, score_cutoff=0, limit=5):
    """Get a list of the best matches to a collection of choices.

    Convenience function for getting the choices with best scores.

    Args:
        query: A string to match against
        choices: A list or dictionary of choices, suitable for use with
            extract().
        processor: Optional function for transforming choices before matching.
            See extract().
        scorer: Scoring function for extract().
        score_cutoff: Optional argument for score threshold. No matches with
            a score less than this number will be returned. Defaults to 0.
        limit: Optional maximum for the number of elements returned. Defaults
            to 5.

    Returns: A a list of (match, score) tuples.
    """
    best_list = extract(query, choices, processor, scorer, limit)
    return list(itertools.takewhile(lambda x: x[1] >= score_cutoff, best_list))


def extractOne(query, choices, processor=None, scorer=None, score_cutoff=0):
    """Find the single best match above a score in a list of choices.

    This is a convenience method which returns the single best choice.
    See extract() for the full arguments list.

    Args:
        query: A string to match against
        choices: A list or dictionary of choices, suitable for use with
            extract().
        processor: Optional function for transforming choices before matching.
            See extract().
        scorer: Scoring function for extract().
        score_cutoff: Optional argument for score threshold. If the best
            match is found, but it is not greater than this number, then
            return None anyway ("not a good enough match").  Defaults to 0.

    Returns:
        A tuple containing a single match and its score, if a match
        was found that was above score_cutoff. Otherwise, returns None.
    """
    best_list = extract(query, choices, processor, scorer, limit=1)
    if len(best_list) > 0 and best_list[0][1] >= score_cutoff:
        return best_list[0]
    return None


def dedupe(contains_dupes, threshold=70, scorer=fuzz.token_set_ratio):
    """This convenience function takes a list of strings containing duplicates and uses fuzzy matching to identify
    and remove duplicates. Specifically, it uses the process.extract to identify duplicates that
    score greater than a user defined threshold. Then, it looks for the longest item in the duplicate list
    since we assume this item contains the most entity information and returns that. It breaks string
    length ties on an alphabetical sort.

    Note: as the threshold DECREASES the number of duplicates that are found INCREASES. This means that the
        returned deduplicated list will likely be shorter. Raise the threshold for fuzzy_dedupe to be less
        sensitive.

    Args:
        contains_dupes: A list of strings that we would like to dedupe.
        threshold: the numerical value (0,100) point at which we expect to find duplicates.
            Defaults to 70 out of 100
        scorer: Optional function for scoring matches between the query and
            an individual processed choice. This should be a function
            of the form f(query, choice) -> int.
            By default, fuzz.token_set_ratio() is used and expects both query and
            choice to be strings.

    Returns:
        A deduplicated list. For example:

            In: contains_dupes = ['Frodo Baggin', 'Frodo Baggins', 'F. Baggins', 'Samwise G.', 'Gandalf', 'Bilbo Baggins']
            In: fuzzy_dedupe(contains_dupes)
            Out: ['Frodo Baggins', 'Samwise G.', 'Bilbo Baggins', 'Gandalf']
        """

    extractor = []

    # iterate over items in *contains_dupes*
    for item in contains_dupes:
        # return all duplicate matches found
        matches = extract(item, contains_dupes, limit=None, scorer=scorer)
        # filter matches based on the threshold
        filtered = [x for x in matches if x[1] > threshold]
        # if there is only 1 item in *filtered*, no duplicates were found so append to *extracted*
        if len(filtered) == 1:
            extractor.append(filtered[0][0])

        else:
            # alpha sort
            filtered = sorted(filtered, key=lambda x: x[0])
            # length sort
            filter_sort = sorted(filtered, key=lambda x: len(x[0]), reverse=True)
            # take first item as our 'canonical example'
            extractor.append(filter_sort[0][0])

    # uniquify *extractor* list
    keys = {}
    for e in extractor:
        keys[e] = 1
    extractor = keys.keys()

    # check that extractor differs from contain_dupes (e.g. duplicates were found)
    # if not, then return the original list
    if len(extractor) == len(contains_dupes):
        return contains_dupes
    else:
        return extractor
