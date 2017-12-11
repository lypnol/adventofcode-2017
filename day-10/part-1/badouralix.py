from runners.python import Submission
from copy import copy

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		circle_size = 256
		circle = list(range(circle_size))
		current_position = 0
		skip_size = 0
		lengths = [int(n) for n in s.split(',')]

		for length in lengths:
			circle_copy = copy(circle)
			for i in range(length):
				circle_copy[(current_position + i) % circle_size] = circle[(current_position + length - 1 - i) % circle_size]
			circle = circle_copy
			current_position = (current_position + length + skip_size) % circle_size
			skip_size += 1

		return circle[0] * circle[1]
