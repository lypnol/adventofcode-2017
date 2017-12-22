from runners.python import Submission


class AyoubSubmission(Submission):

    def run(self, s):
        infected = set()
        lines = s.split('\n')
        n = len(lines)
        for i, line in enumerate(lines):
            for j in range(n):
                if line[j] == '#':
                    x, y = (j - n // 2 , n // 2 - i)
                    infected.add((x, y))
        current = (0, 0)
        direction = (0, 1)
        cause = 0
        for _ in range(10000):
            if current in infected:
                direction = self.turn(direction, 1)
                infected.remove(current)
            else:
                direction = self.turn(direction, -1)
                infected.add(current)
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
