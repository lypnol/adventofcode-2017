import math
from submission import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        line_size = int(math.sqrt(int(s))) + 2
        if line_size % 2 == 0:
            line_size -= 1

        rem = (pow(line_size, 2) - int(s)) % (line_size - 1)

        return (line_size // 2) + abs(line_size // 2 - rem)
