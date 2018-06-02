.. image:: https://travis-ci.org/seatgeek/fuzzywuzzy.svg?branch=master
    :target: https://travis-ci.org/seatgeek/fuzzywuzzy

FuzzyWuzzy
==========

Fuzzy string matching like a boss. It uses `Levenshtein Distance <https://en.wikipedia.org/wiki/Levenshtein_distance>`_ to calculate the differences between sequences in a simple-to-use package.

Requirements
============

-  Python 2.4 or higher
-  difflib
-  `python-Levenshtein <https://github.com/ztane/python-Levenshtein/>`_ (optional, provides a 4-10x speedup in String
   Matching, though may result in `differing results for certain cases <https://github.com/seatgeek/fuzzywuzzy/issues/128>`_)

For testing
~~~~~~~~~~~
-  pycodestyle
-  hypothesis
-  pytest

Installation
============

Using PIP via PyPI

.. code:: bash

    pip install fuzzywuzzy

or the following to install `python-Levenshtein` too

.. code:: bash

    pip install fuzzywuzzy[speedup]


Using PIP via Github

.. code:: bash

    pip install git+git://github.com/seatgeek/fuzzywuzzy.git@0.16.0#egg=fuzzywuzzy

Adding to your ``requirements.txt`` file (run ``pip install -r requirements.txt`` afterwards)

.. code:: bash

    git+ssh://git@github.com/seatgeek/fuzzywuzzy.git@0.16.0#egg=fuzzywuzzy
    
Manually via GIT

.. code:: bash

    git clone git://github.com/seatgeek/fuzzywuzzy.git fuzzywuzzy
    cd fuzzywuzzy
    python setup.py install


Usage
=====

.. code:: python

    >>> from fuzzywuzzy import fuzz
    >>> from fuzzywuzzy import process

Simple Ratio
~~~~~~~~~~~~

.. code:: python

    >>> fuzz.ratio("this is a test", "this is a test!")
        97

Partial Ratio
~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.partial_ratio("this is a test", "this is a test!")
        100

Token Sort Ratio
~~~~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
        91
    >>> fuzz.token_sort_ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
        100

Token Set Ratio
~~~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.token_sort_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
        84
    >>> fuzz.token_set_ratio("fuzzy was a bear", "fuzzy fuzzy was a bear")
        100

Process
~~~~~~~

.. code:: python

    >>> choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]
    >>> process.extract("new york jets", choices, limit=2)
        [('New York Jets', 100), ('New York Giants', 78)]
    >>> process.extractOne("cowboys", choices)
        ("Dallas Cowboys", 90)

You can also pass additional parameters to ``extractOne`` method to make it use a specific scorer. A typical use case is to match file paths:

.. code:: python
  
    >>> process.extractOne("System of a down - Hypnotize - Heroin", songs)
        ('/music/library/good/System of a Down/2005 - Hypnotize/01 - Attack.mp3', 86)
    >>> process.extractOne("System of a down - Hypnotize - Heroin", songs, scorer=fuzz.token_sort_ratio)
        ("/music/library/good/System of a Down/2005 - Hypnotize/10 - She's Like Heroin.mp3", 61)

.. |Build Status| image:: https://api.travis-ci.org/seatgeek/fuzzywuzzy.png?branch=master
   :target: https:travis-ci.org/seatgeek/fuzzywuzzy

Known Ports
============

FuzzyWuzzy is being ported to other languages too! Here are a few ports we know about:

-  Java: `xpresso's fuzzywuzzy implementation <https://github.com/WantedTechnologies/xpresso/wiki/Approximate-string-comparison-and-pattern-matching-in-Java>`_
-  Java: `fuzzywuzzy (java port) <https://github.com/xdrop/fuzzywuzzy>`_
-  Rust: `fuzzyrusty (Rust port) <https://github.com/logannc/fuzzyrusty>`_
-  JavaScript: `fuzzball.js (JavaScript port) <https://github.com/nol13/fuzzball.js>`_
-  C++: `Tmplt/fuzzywuzzy <https://github.com/Tmplt/fuzzywuzzy>`_
-  C#: `fuzzysharp (.Net port) <https://github.com/BoomTownRoi/BoomTown.FuzzySharp>`_
-  Go: `go-fuzzywuzz (Go port) <https://github.com/paul-mannino/go-fuzzywuzzy>`_



