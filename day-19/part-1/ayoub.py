from runners.python import Submission
from collections import deque
from string import ascii_uppercase


class AyoubSubmission(Submission):

    def run(self, s):
        g = []
        for line in s.split('\n'):
            if line.rstrip() == '':
                continue 
            g.append(list(line))
        n, m = len(g), len(g[0])
        start = None
        for j in range(n):
            if g[0][j] == '|':
                start = (0, j)
                break
        move = start
        prev = None
        direction = (1, 0)
        letters = []
        while True:
            if move == prev:
                raise Exception('stuck')
            (i, j) = move
            (u, v) = direction
            if g[i][j] in ascii_uppercase:
                letters.append(g[i][j])
            prev = move
            if not (0 <= i+u < n and 0 <= j+v < m) or g[i+u][j+v] == ' ':
                break
            elif g[i+u][j+v] in ascii_uppercase:
                move = (i+u, j+v)
            elif u == 0 and g[i+u][j+v] == '-':
                move = (i+u, j+v)
            elif u == 0 and g[i+u][j+v] == '|':
                move = (i+u, j+v*2)
            elif v == 0 and g[i+u][j+v] == '|':
                move = (i+u, j+v)
            elif v == 0 and g[i+u][j+v] == '-':
                move = (i+u*2, j+v)
            elif g[i+u][j+v] == '+':
                x, y = i+u, j+v
                for (p, q) in [(v, u), (-v, -u)]:
                    if not (0 <= x+p < n and 0 <= y+q < len(g[x+p])):
                        continue
                    if g[x+p][y+q] != ' ':
                        direction = (p, q)
                        break
                move = (i+u, j+v)
        
        return ''.join(letters)
