from runners.python import Submission

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		steps = int(s)
		iterations = 50000000

		zero_pos = 0
		pos = 0
		value_after_zero = None

		for i in range(1, iterations+1):
			pos = (pos+steps) % i

			if pos < zero_pos:
				zero_pos = (zero_pos + 1) % i
			elif pos == zero_pos:
				value_after_zero = i

			pos += 1

		return value_after_zero
