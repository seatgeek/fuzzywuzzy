Installation
============

Requirements
~~~~~~~~~~~~

-  Python 2.7 or higher
-  difflib
-  `python-Levenshtein <https://github.com/ztane/python-Levenshtein/>`_ (optional, provides a 4-10x speedup in String
   Matching, though may result in `differing results for certain cases <https://github.com/seatgeek/fuzzywuzzy/issues/128>`_)

For testing
-----------

-  pycodestyle
-  hypothesis
-  pytest

Using PIP
~~~~~~~~~

Via PyPI
--------

.. code:: bash

    pip install fuzzywuzzy

or the following to install `python-Levenshtein` too

.. code:: bash

    pip install fuzzywuzzy[speedup]


Via Github
----------

.. code:: bash

    pip install git+git://github.com/seatgeek/fuzzywuzzy.git@0.17.0#egg=fuzzywuzzy

Adding to your ``requirements.txt`` file (run ``pip install -r requirements.txt`` afterwards)

.. code:: bash

    git+ssh://git@github.com/seatgeek/fuzzywuzzy.git@0.17.0#egg=fuzzywuzzy

Manually via GIT
~~~~~~~~~~~~~~~~

.. code:: bash

    git clone git://github.com/seatgeek/fuzzywuzzy.git fuzzywuzzy
    cd fuzzywuzzy
    python setup.py install
