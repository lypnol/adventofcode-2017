from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        return str(sum([int(s[i]) if s[i] == s[(i + 1) % len(s)] else 0 for i in range(len(s))]))
