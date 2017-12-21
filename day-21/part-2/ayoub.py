from runners.python import Submission
import itertools


class AyoubSubmission(Submission):

    def run(self, s):
        rules = {}
        for line in s.split('\n'):
            parts = line.split(' => ')
            state = parts[0]
            result = parts[1]
            rules[state] = result
            for equivalent in self.equivalents(state):
                rules[equivalent] = result
            
        for state in self.gen_all():
            if state in rules:
                continue
            for equivalent in self.equivalents(state):
                if equivalent not in rules:
                    continue
                rules[state] = rules[equivalent]
                break
            if state not in rules:
                raise Exception('Couldn\'t find equivalent in rules')
        
        current = self.str_to_matrix('.#./..#/###')
        iterations = 18
        while iterations:
            n = len(current)
            if n % 2 == 0:
                next_state = [[0 for j in range(n+n//2)] for i in range(n+n//2)]
                for i in range(0, n-1, 2):
                    for j in range(0, n-1, 2):
                        sub = ((current[i][j],   current[i][j+1]), 
                               (current[i+1][j], current[i+1][j+1]))
                        res = self.str_to_matrix(rules[self.matrix_to_str(sub)])
                        for p in range(3):
                            for q in range(3):
                                next_state[p+i+i//2][q+j+j//2] = res[p][q]
            else:
                next_state = [[0 for j in range(n+n//3)] for i in range(n+n//3)]
                for i in range(0, n-2, 3):
                    for j in range(0, n-2, 3):
                        sub = ((current[i][j],   current[i][j+1],   current[i][j+2]), 
                               (current[i+1][j], current[i+1][j+1], current[i+1][j+2]),
                               (current[i+2][j], current[i+2][j+1], current[i+2][j+2]))
                        res = self.str_to_matrix(rules[self.matrix_to_str(sub)])
                        for p in range(4):
                            for q in range(4):
                                next_state[p+i+i//3][q+j+j//3] = res[p][q]
            current = next_state
            iterations -= 1

        n = len(current)
        count = 0
        for i in range(n):
            for j in range(n):
                if current[i][j] == '#':
                    count += 1
        return count

    def gen_all(self):
        states = set()
        for p in itertools.product('.#', repeat=4):
            states.add(p[0]+p[1]+'/'+p[2]+p[3])
        for p in itertools.product('.#', repeat=9):
            states.add(p[0]+p[1]+p[2]+'/'+p[3]+p[4]+p[5]+'/'+p[6]+p[7]+p[8])
        return states

    def str_to_matrix(self, string):
        rows = string.split('/')
        return tuple([tuple(list(r)) for r in rows])

    def matrix_to_str(self, state):
        return '/'.join([''.join(row) for row in state])

    def print_state(self, state):
        for row in state:
            print(''.join(row))

    def equivalents(self, state):
        m = self.str_to_matrix(state)
        n = len(m)
        res = set()
        # rotate
        for degree in [-270, -180, -90, 90, 180, 270]:
            res.add(self.matrix_to_str(rotate(m, degree)))
        # flip
        if n == 2:
            res.add(self.matrix_to_str((m[1], m[0])))
        else:
            res.add(self.matrix_to_str((m[2], m[1], m[0])))

        res.add(self.matrix_to_str([[m[i][n-j-1] for j in range(n)] for i in range(n)]))

        return res

def rotate(matrix, degree):
    if degree == 0:
        return matrix
    elif degree > 0:
        return rotate(tuple([tuple(r) for r in zip(*matrix[::-1])]), degree-90)
    else:
        return rotate(tuple([tuple(r) for r in zip(*matrix[::-1])]), degree+90)