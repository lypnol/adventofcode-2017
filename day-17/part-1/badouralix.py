from runners.python import Submission

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		step_size = int(s)
		max_iter = 2017
		buffer = [0]
		current_position = 0

		for i in range(1, max_iter + 1):
			current_position += step_size
			current_position %= i
			current_position += 1
			buffer = buffer[:current_position] + [i] + buffer[current_position:]

		return buffer[current_position + 1]
