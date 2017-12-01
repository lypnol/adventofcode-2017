from submission import Submission


class MathieuSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        res = 0
        num1 = int(s[-1])
        for num2 in s:
            num2 = int(num2)
            if num1 == num2:
                res += num1
            num1 = num2
        return str(res)
