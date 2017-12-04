import math
from submission import Submission


class SilvestreSubmission(Submission):
    """
    Forte inspiration de badouralix !
    """

    def run(self, s):
        n = int(s)
        square = 1
        while square**2 < n:
            square += 2
        diff = square**2 - n
        offset = abs(square//2 - diff % (square - 1))
        return str(square//2 + offset)
