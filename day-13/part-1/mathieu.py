from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        inputs = [(int(x.split(': ')[0]), int(x.split(': ')[1])) for x in s.split('\n')]
        severity=0
        for layer, depth in inputs:
            if layer % (2*depth-2)==0:
                severity+=layer*depth
        return severity

