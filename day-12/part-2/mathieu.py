import re

from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        inputs = [set(int(d) for d in re.sub(r'\d+ <-> ', '', line).split(',')) for line in s.split('\n')]
        remaining = set(range(len(inputs)))
        group_count = 0
        while remaining:
            group_count += 1
            visited = set()
            to_visit = set()
            program = remaining.pop()
            visited.add(program)
            to_visit.update(inputs[program])
            while to_visit:
                program = to_visit.pop()
                visited.add(program)
                to_visit = to_visit | inputs[program] - visited
            remaining.difference_update(visited)
        return group_count
