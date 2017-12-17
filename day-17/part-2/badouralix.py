from runners.python import Submission

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		step_size = int(s)
		max_iter = 50*1000*1000
		current_position = 0

		for i in range(1, step_size + 1):
			current_position += step_size
			if current_position >= i:
				current_position %= i
			if current_position == 0:
				result = i
			current_position += 1

		for i in range(step_size + 1, max_iter + 1):
			current_position += step_size
			if current_position >= i:
				current_position -= i
			if current_position == 0:
				result = i
			current_position += 1

		return result
