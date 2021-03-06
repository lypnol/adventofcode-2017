from runners.python import Submission
import operator
import string


class JulesSubmission(Submission):

    def run(self, s):

        table = s.split('\n')
        # reformat last line destroyed by rstrip()
        table[-1] = '{0: <{1}}'.format(table[-1], len(table[0]))
        position = (table[0].index('|'), 0)
        direction = (0, 1)
        message = ''

        def change_direction(direction, position, table):
            col = [0, 0, 1, -1]
            row = [-1, 1, 0, 0]
            COLS = len(table[0])
            ROWS = len(table)
            for i in range(len(col)):
                if 0 <= position[0] + col[i] < COLS and 0 <= position[1] + row[i] < ROWS and direction != (-col[i], -row[i]):
                    if(table[position[1] + row[i]][position[0] + col[i]] in '-|' + string.ascii_letters):
                        return (col[i], row[i])
            return (0, 0)

        force_next = False
        steps = 0
        new_steps = 0
        while True:
            while (table[position[1]][position[0]] != '+' and table[position[1]][position[0]] in '-|' + string.ascii_letters) or force_next:
                force_next = False
                position = tuple(map(operator.add, position, direction))
                new_steps += 1
                if table[position[1]][position[0]] in string.ascii_letters:
                    steps += new_steps
                    new_steps = 0
                    message += table[position[1]][position[0]]
            direction = change_direction(direction, position, table)
            force_next = True
            if direction == (0, 0):
                break
        return steps + 1
