from runners.python import Submission

class AlsyiaSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag

		lines = [line.split() for line in s.split('\n')]
		linesInt = [[int(item) for item in line] for line in lines]
		minMaxList = [max(line) - min(line) for line in linesInt]

		return sum(minMaxList)
