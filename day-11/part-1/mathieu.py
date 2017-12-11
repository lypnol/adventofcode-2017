from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        # Inspiré de la façon de "compter" de Xavier
        n_pos = s.count('n')-s.count('s')
        e_pos = s.count('e')-s.count('w')
        return max(abs(n_pos),abs(e_pos))
