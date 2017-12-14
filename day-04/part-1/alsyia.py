from runners.python import Submission

class AlsyiaSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		lines = [line.split() for line in s.split('\n')]
		validLines = 0
		for line in lines:
			if(len(line) == len(set(line))):
				validLines += 1
		return validLines
