from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        count = 0
        for line in s.split('\n'):
            words = line.split()
            unique_words = set(words)
            count = count + 1 if len(words) == len(unique_words) else count
        return count
