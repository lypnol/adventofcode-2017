from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        value_a, value_b = [int(row.split()[-1]) for row in s.split("\n")]

        count = 0
        i = 0
        loop_number = 5000000
        while i < loop_number:
            while True:
                value_a = value_a * 16807 % 2147483647
                if value_a % 4 == 0:
                    break
            while True:
                value_b = value_b * 48271 % 2147483647
                if value_b % 8 == 0:
                    break
            if (value_a & 0xffff) == (value_b  & 0xffff):
                count += 1
            i += 1

        return count
