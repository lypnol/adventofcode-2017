from runners.python import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here


		return str(sum(int(s[i]) for i in range(len(s)) if s[i-1] == s[i]))


