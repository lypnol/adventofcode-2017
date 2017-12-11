from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        n_pos = 0
        e_pos = 0
        for char in s:
            if char == "e":
                e_pos += 1
            elif char == "w":
                e_pos -= 1
            elif char == "n":
                n_pos += 1
            elif char == "s":
                n_pos -= 1
        return max(abs(n_pos),abs(e_pos)
