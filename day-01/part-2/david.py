from runners.python import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		n = len(s)

		return sum(int(s[i]) for i in range(n) if s[i] == s[(i+n//2)%n])

