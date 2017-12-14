from runners.python import Submission

class AlsyiaSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		return sum([int(s[i]) for i in range(len(s)) if s[i] == s[(i + len(s)//2) % len(s)]])
