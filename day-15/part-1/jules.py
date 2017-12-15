from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        lines = s.split('\n')
        genA, genB, n = 16807, 48271, 2147483647
        a = int(lines[0].split()[-1])
        b = int(lines[1].split()[-1])
        i = 0
        score = 0
        while i < 40000000:
            i += 1
            if (a & 0xffff) == (b & 0xffff):
                score += 1
            a = (a * genA) % n
            b = (b * genB) % n
        return score
