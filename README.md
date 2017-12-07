[![Build Status](https://travis-ci.org/lypnol/adventofcode-2017.svg?branch=master)](https://travis-ci.org/lypnol/adventofcode-2017)
# Advent of code 2017 submissions

⁣    🌟
    🎄
   🎄🎄
  🎄⁣🎄🎄
 🎄🎄🎄🎄
🎄🎄🎄🎄🎄
  🎁🎁🎁

These are proposed submissions for http://adventofcode.com/2017.

The solutions are automatically tested with travis

## How to use

To run submissions use `run.py` script

```
usage: run.py [-h] [--last] [-d DAY] [-p PART] [-a AUTHORS] [-i IGNORE]
              [-l LANGUAGES] [-f] [-r] [-s]

Run contest submissions

optional arguments:
  -h, --help            show this help message and exit
  --last                Run submissions from last day
  -d DAY, --day DAY     Run submissions for specific day
  -p PART, --part PART  Run submissions for specific day part
  -a AUTHORS, --authors AUTHORS
                        Run submissions from specific authors, ex: user1,user2
  -i IGNORE, --ignore IGNORE
                        Ignore submissions from specific authors
  -l LANGUAGES, --languages LANGUAGES
                        Run submissions written in specific languages, ex:
                        js,py, supported: py js go rb cpp
  -f, --force           Force running submissions even if tool is missing
  -r, --restricted      Restrict each author to their input only
  -s, --silent          Disable debug mode
```

## How to contribute

For now we support `c++`, `python 3`, `javascript`, `go` and `ruby`.

You can use `create.py` tool to create a new empty submission:

```
usage: create.py [-h] [-p {1,2}] [-l {cpp,py,js,go,rb}] author day

Creates new empty submission

positional arguments:
  author                Name of author (github login)
  day                   Day of problem (between 1 and 25)

optional arguments:
  -h, --help            show this help message and exit
  -p {1,2}, --part {1,2}
                        Create submission for one day part only
  -l {cpp,py,js,go,rb}, --language {cpp,py,js,go,rb}
                        Use specified language
```

### Using python

If you don't use `create.py` tool you should follow this convention:

```bash
day-[number]/part-[number]/[your_login].py          # your submission code
day-[number]/part-[number]/inputs/[your_login].txt  # your input file
```

Your submission code should inherit from the `Submission` class from `runners.python` module:

```python
from runners.python import Submission

class MyAwesomeSubmission(Submission):

    def run(self, s):
    	# :param s: input in string format
    	# :return: solution flag
```

You can add other functions & modules if you need to. Any external dependency should be added to `requirements.txt`.
