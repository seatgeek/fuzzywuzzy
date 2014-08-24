from distutils.core import setup

setup(name='fuzzywuzzy',
      version='0.3.1',
      description='Fuzzy string matching in python',
      long_description=open('README.rst').read(),
      author='Adam Cohen',
      author_email='adam@seatgeek.com',
      url='https://github.com/seatgeek/fuzzywuzzy/',
      packages=['fuzzywuzzy'],
      classifiers=(
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3'
      )
      )
