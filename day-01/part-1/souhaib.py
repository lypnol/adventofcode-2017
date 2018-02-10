from submission import Submission


class SouhaibSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        return sum([int(s[i]) for i in range(-1, len(s) -1) if s[i] == s[i+1]])
        
