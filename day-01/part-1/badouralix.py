from runners.python import Submission


class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		return sum([int(s[i]) for i in range(len(s)) if s[i-1] == s[i]])
