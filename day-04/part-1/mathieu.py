from submission import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        res=0
        for line in s.split('\n'):
            is_valid = True
            for word in line.split():
                if line.count(word)>1:
                    is_valid=False
            res+=is_valid
        return res