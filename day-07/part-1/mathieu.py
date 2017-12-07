from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        inputs = [line.replace(',','').split() for line in s.split('\n')]
        roots = set()
        sons = set()
        for line in inputs:
            if len(line) > 2:
                roots.add(line[0])
                for son in line[3:]:
                    sons.add(son)
        return (roots-sons).pop()


