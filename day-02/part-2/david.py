from runners.python import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here

		lines = s.split("\n")
		lines = [[int(x) for x in l.split()] for l in lines]
		return sum([self.find_line_result(l) for l in lines])


	def find_line_result(self, line):
		n = len(line)
		for i in range(n-1):
			for j in range(i, n):
				if line[i] > line[j] and line[i] % line[j] == 0:
					return line[i]//line[j]
				if line[j] > line[i] and line[j] % line[i] == 0:
					return line[j]//line[i]
