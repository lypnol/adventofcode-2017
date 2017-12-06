from submission import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        banks = [int(x) for x in s.split('\t')]
        n = len(banks)
        history = dict()
        cycle=0
        tpl_banks=tuple(banks)
        while tpl_banks not in history.keys():
            history[tpl_banks]=cycle
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
            tpl_banks = tuple(banks)
        return cycle-history[tpl_banks]
