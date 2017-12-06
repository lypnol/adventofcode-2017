from submission import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        banks = list(map(int, s.split("\t")))
        n = len(banks)
        history = list()
        cycle = 0
        while banks not in history:
            history.append(list(banks))
            buffer = max(banks)
            chosen_bank = banks.index(max(banks))
            banks[chosen_bank] -= buffer
            i = (chosen_bank + 1) % n
            while buffer > 0:
                banks[i] += 1
                i = (i + 1) % n
                buffer -= 1
            cycle += 1
        return cycle
