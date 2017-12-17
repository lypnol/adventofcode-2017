from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        step = int(s)
        i = 1
        circular_buffer = [0]
        current_pos = 0
        while i <= 2017:
            current_pos = (current_pos + step) % i + 1
            circular_buffer.insert(current_pos, i)
            i += 1
        return circular_buffer[(current_pos + 1) % i]
