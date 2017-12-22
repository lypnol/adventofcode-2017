from runners.python import Submission
from collections import defaultdict


class AyoubSubmission(Submission):

    def run(self, s):
        state = defaultdict(lambda:0)
        lines = s.split('\n')
        n = len(lines)
        for i, line in enumerate(lines):
            for j in range(n):
                if line[j] == '#':
                    x, y = (j - n // 2 , n // 2 - i)
                    state[(x, y)] = 2
        current = (0, 0)
        direction = (0, 1)
        cause = 0
        for _ in range(10000000):
            if state[current] == 0:
                direction = self.turn(direction, -1)
            elif state[current] == 2:
                direction = self.turn(direction, 1)
            elif state[current] == 3:
                direction = (-direction[0], -direction[1])
            state[current] = (state[current] + 1)%4
            if state[current] == 2:
                cause += 1
            current = (current[0] + direction[0], current[1] + direction[1])

        return cause

    
    def turn(self, direction, sign):
        u, v = direction
        # up
        if v == 1:
            return (sign*1, 0)
        # down
        elif v == -1:
            return (-sign*1, 0)
        # left
        elif u == -1:
            return (0, sign*1)
        # right
        elif u == 1:
            return (0, -sign*1)
