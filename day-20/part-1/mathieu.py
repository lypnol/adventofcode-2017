import re

from runners.python import Submission


class MathieuSubmission(Submission):
    def re_acceleration(self, line):
        groups = re.search(r'a=<(-?\d+),(-?\d+),(-?\d+)>', line)
        return sum(abs(int(acc)) for acc in groups.group(1, 2, 3))

    def run(self, s):
        abs_accelerations = [self.re_acceleration(line) for line in s.split('\n')]
        return abs_accelerations.index(min(abs_accelerations))
