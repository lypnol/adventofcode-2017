[![Build Status](https://travis-ci.org/lypnol/adventofcode-2017.svg?branch=master)](https://travis-ci.org/lypnol/adventofcode-2017)
# Advent of code 2017 submissions

These are proposed submissions for http://adventofcode.com/2017.

The solutions are automatically tested with travis

## How to use

```
usage: main.py [-h] [--last] [-d DAY] [-p PART] [-a AUTHORS] [-i IGNORE] [-r]
               [-v]

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
  -r, --restricted      Restricts inputs on specified author
  -v, --verbose         Enable debug mode
```


## How to contribute

For now we only support `python 3`.  
To add your solution you should follow this convention:
```
day-[number]/part-[number]/[your_login].py 			# your submission code
day-[number]/part-[number]/inputs/[your_login].txt 	# your input file
```

check the [https://github.com/lypnol/adventofcode-2016](2016) edition to see examples.

Your submission code should inherit from the `Submission` class from `submission.py` file:

```python
from submission import Submission


class MyAwesomeSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
    	# :param s: input in string format
    	# :return: solution flag
```

