|Build Status|

FuzzyWuzzy
==========

Fuzzy string matching like a boss.

Requirements
============

-  Python 2.4 or higher
-  difflib
-  python-Levenshtein (optional, provides a 4-10x speedup in String
   Matching)

Installation
============

Using PIP via PyPI

.. code:: bash

    pip install fuzzywuzzy

Using PIP via Github

.. code:: bash

    pip install git+git://github.com/seatgeek/fuzzywuzzy.git@0.7.0#egg=fuzzywuzzy

Adding to your ``requirements.txt`` file (run ``pip install -r requirements.txt`` afterwards)

.. code:: bash

    git+ssh://git@github.com/seatgeek/fuzzywuzzy.git@0.7.0#egg=fuzzywuzzy
    
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
        96

Partial Ratio
~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.partial_ratio("this is a test", "this is a test!")
        100

Token Sort Ratio
~~~~~~~~~~~~~~~~

.. code:: python

    >>> fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
        90
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

.. |Build Status| image:: https://api.travis-ci.org/seatgeek/fuzzywuzzy.png?branch=master
   :target: https:travis-ci.org/seatgeek/fuzzywuzzy

Known Ports
============
Some people are porting FuzzyWuzzy to other languages. Here is one port we know about:

-  Java: https://github.com/WantedTechnologies/xpresso/wiki/Approximate-string-comparison-and-pattern-matching-in-Java
