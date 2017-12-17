from runners.python import Submission

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		steps = int(s)
		iterations = 2017

		buffer = [0]
		pos = 0

		for i in range(1, iterations+1):
			pos = (pos+steps) % i
			buffer = buffer[:pos+1] + [i] + buffer[pos+1:]
			pos += 1

		return buffer[pos+1]





