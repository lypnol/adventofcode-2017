from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        return str(sum([max([int(x) for x in row.split()]) - min([int(x) for x in row.split()]) for row in s.split('\n')]))
