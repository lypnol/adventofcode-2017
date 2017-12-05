from runners.python import Submission


class CocoSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		return sum([int(s[i]) for i in range(len(s)) if s[i] == s[int(i+len(s)/2) % len(s)]])

