from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        step = int(s)
        i = 1
        current_pos = 0
        while i <= 50000000:
            current_pos = (current_pos + step) % i + 1
            if current_pos == 1:
                ret = i
            i += 1
        return ret
