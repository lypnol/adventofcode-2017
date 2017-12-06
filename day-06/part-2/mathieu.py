from submission import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        banks = [int(x) for x in s.split()]
        n = len(banks)
        history = dict()
        cycle=0
        while tuple(banks) not in history.keys():
            history[tuple(banks)]=cycle
            buffer = max(banks)
            i = banks.index(buffer)
            banks[i] = 0
            while buffer > 0:
                i += 1
                if i == n:
                    i = 0
                banks[i] += 1
                buffer -= 1
            cycle+=1
        return cycle-history[tuple(banks)]
