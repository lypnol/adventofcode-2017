from runners.python import Submission
from collections import Counter

class BadouralixSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        steps = Counter(s.split(','))
        group_law = [
            ('n',  's',  ''),
            ('ne', 'sw', ''),
            ('nw', 'se', ''),
            ('n',  'sw', 'nw'),
            ('n',  'se', 'ne'),
            ('s',  'nw', 'sw'),
            ('s',  'ne', 'se'),
            ('ne', 'nw', 'n'),
            ('se', 'sw', 's'),
        ]
        reducible = True

        while reducible:
            reducible = False
            for action in group_law:
                if steps[action[0]] > 0 and steps[action[1]] > 0:
                    reducible = True
                    iterations = min(steps[action[0]], steps[action[1]])
                    steps -= Counter({action[0]:iterations, action[1]:iterations, action[2]:-iterations})

        del steps['']
        return sum(steps.values())
