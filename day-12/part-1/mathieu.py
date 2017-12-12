import re

from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        inputs = [set(int(d) for d in re.sub(r'\d+ <-> ', '', line).split(',')) for line in s.split('\n')]
        visited = set([0])
        to_visit = set(inputs[0])
        while to_visit:
            program = to_visit.pop()
            visited.add(program)
            to_visit = to_visit | inputs[program] - visited
        return len(visited)
