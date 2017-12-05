from runners.python import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here

		lines = s.split("\n")
		integers = [[int(x) for x in l.split()] for l in lines]
		return sum((max(l) - min(l)) for l in integers)
