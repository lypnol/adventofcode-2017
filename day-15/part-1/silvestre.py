from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        value_a, value_b = [int(row.split()[-1]) for row in s.split("\n")]

        count = 0
        i = 0
        loop_number = 40000000
        while i < loop_number:
            value_a = value_a * 16807 % 2147483647
            value_b = value_b * 48271 % 2147483647
            #import pdb; pdb.set_trace()
            if (value_a & 0xffff) == (value_b  & 0xffff):
                count += 1
            i += 1

        return count
