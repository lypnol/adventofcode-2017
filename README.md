[![Build Status](https://travis-ci.org/lypnol/adventofcode-2017.svg?branch=master)](https://travis-ci.org/lypnol/adventofcode-2017)
# Advent of code 2017 submissions

These are proposed submissions for http://adventofcode.com/2017.

The solutions are automatically tested with travis

## How to use

To run submissions use `run.py` script
```
usage: run.py [-h] [--last] [-d DAY] [-p PART] [-a AUTHORS] [-i IGNORE] [-r]
              [-s]

Runs contest submissions

optional arguments:
  -h, --help            show this help message and exit
  --last                Runs submissions from last day
  -d DAY, --day DAY     Runs submissions for specific day
  -p PART, --part PART  Runs submissions for specific day part
  -a AUTHORS, --authors AUTHORS
                        Runs submissions from specific authors, ex:
                        user1,user2
  -i IGNORE, --ignore IGNORE
                        Ignores submissions from specific authors
  -r, --restricted      Restricts each author to their input only
  -s, --silent          Disable debug mode
```

## How to contribute

For now we only support `python 3`.  

You can use `create.py` tool to create a new empty submission:
```
usage: create.py [-h] [-p {1,2}] author day

Creates new empty submission

positional arguments:
  author                Name of author (github login)
  day                   Day of problem (between 1 and 25)

optional arguments:
  -h, --help            show this help message and exit
  -p {1,2}, --part {1,2}
                        Create submission for one day part only
```

To add your solution you should follow this convention:
```
day-[number]/part-[number]/[your_login].py          # your submission code
day-[number]/part-[number]/inputs/[your_login].txt  # your input file
```

Your submission code should inherit from the `Submission` class from `submission.py` file:
```python
from submission import Submission


class MyAwesomeSubmission(Submission):

    def run(self, s):
    	# :param s: input in string format
    	# :return: solution flag
```

