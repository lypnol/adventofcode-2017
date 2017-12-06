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

For now we only support `python 3`, `javascript` and `go`.

You can use `create.py` tool to create a new empty submission:

```
usage: create.py [-h] [-p {1,2}] [-l {py,js,go}] author day

Creates new empty submission

positional arguments:
  author                Name of author (github login)
  day                   Day of problem (between 1 and 25)

optional arguments:
  -h, --help            show this help message and exit
  -p {1,2}, --part {1,2}
                        Create submission for one day part only
  -l {py,js}, --language {py,js}
                        Use specified language
```

### Using python

If you don't use `create.py` tool you should follow this convention:

```bash
day-[number]/part-[number]/[your_login].py          # your submission code
day-[number]/part-[number]/inputs/[your_login].txt  # your input file
```

Your submission code should inherit from the `Submission` class from `submission.py` file:

```python
from runners.python import Submission

class MyAwesomeSubmission(Submission):

    def run(self, s):
    	# :param s: input in string format
    	# :return: solution flag
```

You can add other functions & modules if you need to. Any external dependency should be added to `requirements.txt`.

### Using javascript

Similar to python, you can use `create.py` tool with the flag `-l js`, which will create the submission files.
Your submission code must implement a function `run`

```javascript
/**
 * @param {string} s puzzle input in string format
 * @returns solution flag
 */
run = s => {
  // Your code goes here
};
```

You can add other functions if you need to.
Any external dependency should be installed with `npm install --save [your dependency]` to be added into `package.json` file.
`userscorejs` is already installed.

### Using go

Similar to javascript, you can use `create.py` tool with the flag `-l go`, which will create the submission files.
Your submission code must take the input as a program argument and print the integer result to stdout

```go
package main

import (
    "fmt"
    "os"
)

func run(s string) int {
    // Your code goes here
}

func main() {
    fmt.Println(run(os.Args[1]))
}
```
