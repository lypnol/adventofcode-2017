from runners.python import Submission


class MathieuSubmission(Submission):

    def run(self, s):
        steps = list(map(int, s.split("\n")))
        n = len(steps)
        i = 0
        step_nb = 0
        while 0 <= i < n:
            new_i = steps[i] + i
            if steps[i]>2:
                steps[i] -= 1
            else:
                steps[i]+=1
            step_nb += 1
            i = new_i
        return step_nb
