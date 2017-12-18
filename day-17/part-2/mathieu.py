from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        step = int(s)
        current_pos = 0
        ret = 0
        for i in range(1, 50000001):
            current_pos = (current_pos + step) % i + 1
            if current_pos == 1:
                ret = i
        return ret
