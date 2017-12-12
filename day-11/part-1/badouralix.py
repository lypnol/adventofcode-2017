from runners.python import Submission
from collections import Counter

class BadouralixSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        steps = Counter(s.split(','))
        reducible = True

        while reducible:
            if steps['n'] > 0 and steps['s'] > 0:
                iterations = min(steps['n'], steps['s'])
                steps -= Counter(n=iterations, s=iterations)
            elif steps['ne'] > 0 and steps['sw'] > 0:
                iterations = min(steps['ne'], steps['sw'])
                steps -= Counter(ne=iterations, sw=iterations)
            elif steps['nw'] > 0 and steps['se'] > 0:
                iterations = min(steps['nw'], steps['se'])
                steps -=  Counter(nw=iterations, se=iterations)
            elif steps['n'] > 0 and steps['sw'] > 0:
                iterations = min(steps['n'], steps['sw'])
                steps -=  Counter(n=iterations, sw=iterations, nw=-iterations)
            elif steps['n'] > 0 and steps['se'] > 0:
                iterations = min(steps['n'], steps['se'])
                steps -=  Counter(n=iterations, se=iterations, ne=-iterations)
            elif steps['s'] > 0 and steps['nw'] > 0:
                iterations = min(steps['s'], steps['nw'])
                steps -=  Counter(s=iterations, nw=iterations, sw=-iterations)
            elif steps['s'] > 0 and steps['ne'] > 0:
                iterations = min(steps['s'], steps['ne'])
                steps -=  Counter(s=iterations, ne=iterations, se=-iterations)
            elif steps['ne'] > 0 and steps['nw'] > 0:
                iterations = min(steps['ne'], steps['nw'])
                steps -=  Counter(ne=iterations, nw=iterations, n=-iterations)
            elif steps['se'] > 0 and steps['sw'] > 0:
                iterations = min(steps['se'], steps['sw'])
                steps -=  Counter(se=iterations, sw=iterations, s=-iterations)
            else:
                reducible = False

        # print(steps)
        return sum(steps.values())
