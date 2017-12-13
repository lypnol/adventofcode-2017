from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        inputs = [(int(x.split(': ')[0]), int(x.split(': ')[1])) for x in s.split('\n')]
        delay = 0
        caught = True
        while caught:
            caught = False
            for layer, depth in inputs:
                if (delay + layer) % (2 * depth - 2) == 0:
                    caught = True
                    delay += 1
                    break
        return delay
