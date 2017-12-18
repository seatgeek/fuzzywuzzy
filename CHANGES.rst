Changelog
=========

0.16.0 (2017-12-18)
-------------------

- Add punctuation characters back in so process does something.
  [davidcellis]

- Simpler alphabet and even fewer examples. [davidcellis]

- Fewer examples and larger deadlines for Hypothesis. [davidcellis]

- Slightly more examples. [davidcellis]

- Attempt to fix the failing 2.7 and 3.6 python tests. [davidcellis]

- Readme: add link to C++ port. [Lizard]

- Fix tests on Python 3.3. [Jon Banafato]

  Modify tox.ini and .travis.yml to install enum34 when running with
  Python 3.3 to allow hypothesis tests to pass.


- Normalize Python versions. [Jon Banafato]

  - Enable Travis-CI tests for Python 3.6
  - Enable tests for all supported Python versions in tox.ini
  - Add Trove classifiers for Python 3.4 - 3.6 to setup.py

  ---

  Note: Python 2.6 and 3.3 are no longer supported by the Python core
  team. Support for these can likely be dropped, but that's out of scope
  for this change set.


- Fix typos. [Sven-Hendrik Haase]

0.15.1 (2017-07-19)
-------------------

- Fix setup.py (addresses #155) [Paul O'Leary McCann]

- Merge remote-tracking branch 'upstream/master' into
  extract_optimizations. [nolan]

- Seed random before generating benchmark strings. [nolan]

- Cleaner implementation of same idea without new param, but adding
  existing full_process param to Q,W,UQ,UW. [nolan]

- Fix benchmark only generate list once. [nolan]

- Only run util.full_process once on query when using extract functions,
  add new benchmarks. [nolan]

0.15.0 (2017-02-20)
-------------------

- Add extras require to install python-levenshtein optionally. [Rolando
  Espinoza]

  This allows to install python-levenshtein as dependency.


- Fix link formatting in the README. [Alex Chan]

- Add fuzzball.js JavaScript port link. [nolan]

- Added Rust Port link. [Logan Collins]

- Validate_string docstring. [davidcellis]

- For full comparisons test that ONLY exact matches (after processing)
  are added. [davidcellis]

- Add detailed docstrings to WRatio and QRatio comparisons.
  [davidcellis]

0.14.0 (2016-11-04)
-------------------

- Possible PEP-8 fix + make pep-8 warnings appear in test. [davidcellis]

- Possible PEP-8 fix. [davidcellis]

- Possible PEP-8 fix. [davidcellis]

- Test for stderr log instead of warning. [davidcellis]

- Convert warning.warn to logging.warning. [davidcellis]

- Additional details for empty string warning from process.
  [davidcellis]

  String formatting fix for python 2.6


- Enclose warnings.simplefilter() inside a with statement. [samkennerly]

0.13.0 (2016-11-01)
-------------------

- Support alternate git status output. [Jose Diaz-Gonzalez]

- Split warning test into new test file, added to travis execution on
  2.6 / pypy3. [davidcellis]

- Remove hypothesis examples database from gitignore. [davidcellis]

- Add check for warning to tests. [davidcellis]

  Reordered test imports


- Check processor and warn before scorer may remove processor.
  [davidcellis]

- Renamed test - tidied docstring. [davidcellis]

- Add token ratios to the list of scorers that skip running full_process
  as a processor. [davidcellis]

- Added tokex_sort, token_set to test. [davidcellis]

- Test docstrings/comments. [davidcellis]

  Removed redundant check from test.


- Added py.test .cache/ removed duplicated build from gitignore.
  [davidcellis]

- Added default_scorer, default_processor parameters to make it easier
  to change in the future. [davidcellis]

  Added warning if the processor reduces the input query to an empty string.


- Rewrote extracts to explicitly use default values for processor and
  scorer. [davidcellis]

- Changed Hypothesis tests to use pytest parameters. [davidcellis]

- Added Hypothesis based tests for identical strings. [Ducksual]

  Added support for hypothesis to travis config.
  Hypothesis based tests are skipped on Python 2.6 and pypy3.

  Added .hypothesis/ folder to gitignore


- Added test for simple 'a, b' string on process.extractOne. [Ducksual]

- Process the query in process.extractWithoutOrder when using a scorer
  which does not do so. [Ducksual]

  Closes 139


- Mention that difflib and levenshtein results may differ. [Jose Diaz-
  Gonzalez]

  Closes #128

0.12.0 (2016-09-14)
-------------------

- Declare support for universal wheels. [Thomas Grainger]

- Clarify that license is GPLv2. [Gareth Tan]

0.11.1 (2016-07-27)
-------------------

- Add editorconfig. [Jose Diaz-Gonzalez]

- Added tox.ini cofig file for easy local multi-environment testing
  changed travis config to use py.test like tox updated use of pep8
  module to pycodestyle. [Pedro Rodrigues]

0.11.0 (2016-06-30)
-------------------

- Clean-up. [desmaisons_david]

- Improving performance. [desmaisons_david]

- Performance Improvement. [desmaisons_david]

- Fix link to Levenshtein. [Brian J. McGuirk]

- Fix readme links. [Brian J. McGuirk]

- Add license to StringMatcher.py. [Jose Diaz-Gonzalez]

  Closes #113

0.10.0 (2016-03-14)
-------------------

- Handle None inputs same as empty string (Issue #94) [Nick Miller]

0.9.0 (2016-03-07)
------------------

- Pull down all keys when updating local copy. [Jose Diaz-Gonzalez]

0.8.2 (2016-02-26)
------------------

- Remove the warning for "slow" sequence matcher on PyPy. [Julian
  Berman]

  where it's preferable to use the pure-python implementation.

0.8.1 (2016-01-25)
------------------

- Minor release changes. [Jose Diaz-Gonzalez]

- Clean up wiki link in readme. [Ewan Oglethorpe]

0.8.0 (2015-11-16)
------------------

- Refer to Levenshtein distance in readme. Closes #88. [Jose Diaz-
  Gonzalez]

- Added install step for travis to have pep8 available. [Pedro
  Rodrigues]

- Added a pep8 test. The way I add the error 501 to the ignore tuple is
  probably wrong but from the docs and source code of pep8 I could not
  find any other way. [Pedro Rodrigues]

  I also went ahead and removed the pep8 call from the release file.


- Added python 3.5, pypy, and ypyp3 to the travis config file. [Pedro
  Rodrigues]

- Added another step to the release file to run the tests before
  releasing. [Pedro Rodrigues]

- Fixed a few pep8 errors Added a verification step in the release
  automation file. This step should probably be somewhere at git level.
  [Pedro Rodrigues]

- Pep8. [Pedro Rodrigues]

- Leaving TODOs in the code was never a good idea. [Pedro Rodrigues]

- Changed return values to be rounded integers. [Pedro Rodrigues]

- Added a test with the recovered data file. [Pedro Rodrigues]

- Recovered titledata.csv. [Pedro Rodrigues]

- Move extract test methods into the process test. [Shale Craig]

  Somehow, they ended up in the `RatioTest`, despite asserting that the
  `ProcessTest` works.


0.7.0 (2015-10-02)
------------------

- Use portable syntax for catching exception on tests. [Luis Madrigal]

- [Fix] test against correct variable. [Luis Madrigal]

- Add unit tests for validator decorators. [Luis Madrigal]

- Move validators to decorator functions. [Luis Madrigal]

  This allows easier composition and IMO makes the functions more readable


- Fix typo: dictionery -> dictionary. [shale]

- FizzyWuzzy -> FuzzyWuzzy typo correction. [shale]

- Add check for gitchangelog. [Jose Diaz-Gonzalez]

0.6.2 (2015-09-03)
------------------

- Ensure the rst-lint binary is available. [Jose Diaz-Gonzalez]

0.6.1 (2015-08-07)
------------------

- Minor whitespace changes for PEP8. [Jose Diaz-Gonzalez]

0.6.0 (2015-07-20)
------------------

- Added link to a java port. [Andriy Burkov]

- Patched "name 'unicode' is not defined" python3. [Carlos Garay]

  https://github.com/seatgeek/fuzzywuzzy/issues/80

- Make process.extract accept {dict, list}-like choices. [Nathan
  Typanski]

  Previously, process.extract expected lists or dictionaries, and tested
  this with isinstance() calls. In keeping with the spirit of Python (duck
  typing and all that), this change enables one to use extract() on any
  dict-like object for dict-like results, or any list-like object for
  list-like results.

  So now we can (and, indeed, I've added tests for these uses) call
  extract() on things like:

  - a generator of strings ("any iterable")
  - a UserDict
  - custom user-made classes that "look like" dicts
    (or, really, anything with a .items() method that behaves like a dict)
  - plain old lists and dicts

  The behavior is exactly the same for previous use cases of
  lists-and-dicts.

  This change goes along nicely with PR #68, since those docs suggest
  dict-like behavior is valid, and this change makes that true.


- Merge conflict. [Adam Cohen]

- Improve docs for fuzzywuzzy.process. [Nathan Typanski]

  The documentation for this module was dated and sometimes inaccurate.
  This overhauls the docs to accurately describe the current module,
  including detailing optional arguments that were not previously
  explained - e.g., limit argument to extract().

  This change follows the Google Python Style Guide, which may be found
  at:

  <https://google-styleguide.googlecode.com/svn/trunk/pyguide.html?showone=Comments#Comments>


0.5.0 (2015-02-04)
------------------

- FIX: 0.4.0 is released, no need to specify 0.3.1 in README. [Josh
  Warner (Mac)]

- Fixed a small typo. [Rostislav Semenov]

- Reset `processor` and `scorer` defaults to None with argument
  checking. [foxxyz]

- Catch generators without lengths. [Jeremiah Lowin]

- Fixed python3 issue and deprecated assertion method. [foxxyz]

- Fixed some docstrings, typos, python3 string method compatibility,
  some errors that crept in during rebase. [foxxyz]

- [mod] The lamdba in extract is not needed. [Olivier Le Thanh Duong]

  [mod] Pass directly the defaults functions in the args

  [mod] itertools.takewhile() can handle empty list just fine no need to test for it

  [mod] Shorten extractOne by removing double if

  [mod] Use a list comprehention in extract()

  [mod] Autopep8 on process.py

  [doc] Document make_type_consistent

  [mod] bad_chars shortened

  [enh] Move regex compilation outside the method, otherwhise we don't get the benefit from it

  [mod] Don't need all the blah just to redefine method from string module

  [mod] Remove unused import

  [mod] Autopep8 on string_processing.py

  [mod] Rewrote asciidammit without recursion to make it more readable

  [mod] Autopep8 on utils.py

  [mod] Remove unused import

  [doc] Add some doc to fuzz.py

  [mod] Move the code to sort string in a separate function

  [doc] Docstrings for WRatio, UWRatio


- Add note on which package to install. Closes #67. [Jose Diaz-Gonzalez]

0.4.0 (2014-10-31)
------------------

- In extarctBests() and extractOne() use '>=' instead of '>' [Юрий
  Пайков]

- Fixed python3 issue with SequenceMatcher import. [Юрий Пайков]

0.3.3 (2014-10-22)
------------------

- Fixed issue #59 - "partial" parameter for `_token_set()` is now
  honored. [Юрий Пайков]

- Catch generators without lengths. [Jeremiah Lowin]

- Remove explicit check for lists. [Jeremiah Lowin]

  The logic in `process.extract()` should support any Python sequence/iterable. The explicit check for lists is unnecessary and limiting (for example, it forces conversion of generators and other iterable classes to lists).

0.3.2 (2014-09-12)
------------------

- Make release command an executable. [Jose Diaz-Gonzalez]

- Simplify MANIFEST.in. [Jose Diaz-Gonzalez]

- Add a release script. [Jose Diaz-Gonzalez]

- Fix readme codeblock. [Jose Diaz-Gonzalez]

- Minor formatting. [Jose Diaz-Gonzalez]

- Use __version__ from fuzzywuzzy package. [Jose Diaz-Gonzalez]

- Set __version__ constant in __init__.py. [Jose Diaz-Gonzalez]

- Rename LICENSE to LICENSE.txt. [Jose Diaz-Gonzalez]

0.3.0 (2014-08-24)
------------------

- Test dict input to extractOne() [jamesnunn]

- Remove whitespace. [jamesnunn]

- Choices parameter for extract() accepts both dict and list objects.
  [jamesnunn]

- Enable automated testing with Python 3.4. [Corey Farwell]

- Fixed typo: lettters -> letters. [Tal Einat]

- Fixing LICENSE and README's license info. [Dallas Gutauckis]

- Proper ordered list. [Jeff Paine]

- Convert README to rst. [Jeff Paine]

- Add requirements.txt per discussion in #44. [Jeff Paine]

- Add LICENSE TO MANIFEST.in. [Jeff Paine]

- Rename tests.py to more common test_fuzzywuzzy.py. [Jeff Paine]

- Add proper MANIFEST template. [Jeff Paine]

- Remove MANIFEST file Not meant to be kept in version control. [Jeff
  Paine]

- Remove unused file. [Jeff Paine]

- Pep8. [Jeff Paine]

- Pep8 formatting. [Jeff Paine]

- Pep8 formatting. [Jeff Paine]

- Pep8 indentations. [Jeff Paine]

- Pep8 cleanup. [Jeff Paine]

- Pep8. [Jeff Paine]

- Pep8 cleanup. [Jeff Paine]

- Pep8 cleanup. [Jeff Paine]

- Pep8 import style. [Jeff Paine]

- Pep8 import ordering. [Jeff Paine]

- Pep8 import ordering. [Jeff Paine]

- Remove unused module. [Jeff Paine]

- Pep8 import ordering. [Jeff Paine]

- Remove unused module. [Jeff Paine]

- Pep8 import ordering. [Jeff Paine]

- Remove unused imports. [Jeff Paine]

- Remove unused module. [Jeff Paine]

- Remove import * where present. [Jeff Paine]

- Avoid import * [Jeff Paine]

- Add Travis CI badge. [Jeff Paine]

- Remove python 2.4, 2.5 from Travis (not supported) [Jeff Paine]

- Add python 2.4 and 2.5 to Travis. [Jeff Paine]

- Add all supported python versions to travis. [Jeff Paine]

- Bump minor version number. [Jeff Paine]

- Add classifiers for python versions. [Jeff Paine]

- Added note about python-Levenshtein speedup. Closes #34. [Jose Diaz-
  Gonzalez]

- Fixed tests on 2.6. [Grigi]

- Fixed py2.6. [Grigi]

- Force bad_chars to ascii. [Grigi]

- Since importing unicode_literals, u decorator not required on strings
  from py2.6 and up. [Grigi]

- Py3 support without 2to3. [Grigi]

- Created: Added .travis.yml. [futoase]

- [enh] Add docstrings to process.py. [Olivier Le Thanh Duong]

  Turn the existings comments into docstrings so they can be seen via introspection


- Don't condense multiple punctuation characters to a single whitespace.
  this is a behavioral change. [Adam Cohen]

- UQRatio and UWRatio shorthands. [Adam Cohen]

- Version 0.2. [Adam Cohen]

- Unicode/string comparison bug. [Adam Cohen]

- To maintain backwards compatibility, default is to force_ascii as
  before. [Adam Cohen]

- Fix merge conflict. [Adam Cohen]

- New process function: extractBests. [Flávio Juvenal]

- More readable reverse sorting. [Flávio Juvenal]

- Further honoring of force_ascii. [Adam Cohen]

- Indentation fix. [Adam Cohen]

- Handle force_ascii in fuzz methods. [Adam Cohen]

- Add back relevant tests. [Adam Cohen]

- Utility method to make things consistent. [Adam Cohen]

- Re-commit asciidammit and add a parameter to full_process to determine
  behavior. [Adam Cohen]

- Added a test for non letters/digits replacements. [Tristan Launay]

- ENG-741 fixed benchmark line length. [Laurent Erignoux]

- Fixed Unicode flag for tests. [Tristan Launay]

- ENG-741 commented code removed not erased for review from creator.
  [Laurent Erignoux]

- ENG-741 cut long lines in fuzzy wizzy benchmark. [Laurent Erignoux]

- Re-upped the limit on benchmark, now that performance is not an issue
  anymore. [Tristan Launay]

- Fixed comment. [Tristan Launay]

- Simplified processing of strings with built-in regex code in python.
  Also fixed empty string detection in token_sort_ratio. [Tristan
  Launay]

- Proper benchmark display. Introduce methods to explicitly do all the
  unicode preprocessing *before* using fuzz lib. [Tristan Launay]

- ENG-741: having a true benchmark, to see when we improve stuff.
  [Benjamin Combourieu]

- Unicode support in benchmark.py. [Benjamin Combourieu]

- Added file for processing strings. [Tristan Launay]

- Uniform treatment of strings in Unicode. Non-ASCII chars are now
  considered in strings, which allows for matches in Cyrillic, Chinese,
  Greek, etc. [Tristan Launay]

- Fixed bug in _token_set. [Michael Edward]

- Removed reference to PR. [Jose Diaz-Gonzalez]

- Sadist build and virtualenv dirs are not part of the project. [Pedro
  Rodrigues]

- Fixes https://github.com/seatgeek/fuzzywuzzy/issues/10 and correctly
  points to README.textile. [Pedro Rodrigues]

- Info on the pull request. [Pedro Rodrigues]

- Pullstat.us button. [Pedro Rodrigues]

- Fuzzywuzzy really needs better benchmarks. [Pedro Rodrigues]

- Moved tests and benchmarks out of the package. [Pedro Rodrigues]

- Report better ratio()s redundant import try. [Pedro Rodrigues]

- AssertGreater did not exist in python 2.4. [Pedro Rodrigues]

- Remove debug output. [Adam Cohen]

- Looks for python-Levenshtein package, and if present, uses that
  instead of difflib. 10x speedup if present. add benchmarks. [Adam
  Cohen]

- Add gitignore. [Adam Cohen]

- Fix a bug in WRatio, as well as an issue in full_process, which was
  failing on strings with all unicode characters. [Adam Cohen]

- Error in partial_ratio. closes #7. [Adam Cohen]

- Adding some real-life event data for benchmarking. [Adam Cohen]

- Cleaned up utils.py. [Pedro Rodrigues]

- Optimized speed for full_process() [Pedro Rodrigues]

- Speed improvements to asciidammit. [Pedro Rodrigues]

- Removed old versions of validate_string() and remove_ponctuation()
  kept from previous commits. [Pedro Rodrigues]

- Issue #6 from github updated license headers to match MIT license.
  [Pedro Rodrigues]

- Clean up. [Pedro Rodrigues]

- Changes to utils.validate_string() and benchmarks. [Pedro Rodrigues]

- Some benchmarks to test the changes made to remove_punctuation. [Pedro
  Rodrigues]

- Faster remove_punctuation. [Pedro Rodrigues]

- AssertIsNone did not exist in Python 2.4. [Pedro Rodrigues]

- Just adding some simple install instructions for pip. [Chris Dary]

- Check for null/empty strings in QRatio and WRatio. Add tests. Closes
  #3. [Adam Cohen]

- More README. [Adam Cohen]

- README. [Adam Cohen]

- README. [Adam Cohen]

- Slight change to README. [Adam Cohen]

- Some readme. [Adam Cohen]

- Distutils. [Adam Cohen]

- Change directory structure. [Adam Cohen]

- Initial commit. [Adam Cohen]


