from submission import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        step = len(s) // 2
        res = 0
        for i in range(step):
            if s[i] == s[i + step]:
                res += int(s[i])
        return str(2*res)
