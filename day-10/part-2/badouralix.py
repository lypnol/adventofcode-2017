from runners.python import Submission
from copy import copy

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		circle = list(range(256))
		lengths = [ord(c) for c in s] + [17, 31, 73, 47, 23]
		current_position = 0
		skip_size = 0

		for i in range(64):
			circle, current_position, skip_size = self.round(circle, lengths, current_position, skip_size)

		output = ""
		for i in range(16):
			xor = 0
			for j in range(16):
				xor ^= circle[16*i + j]
			output += "{0:0{1}x}".format(xor,2)

		return output


	def round(self, circle, lengths, current_position, skip_size):
		circle_size = len(circle)

		for length in lengths:
			circle_copy = copy(circle)
			for i in range(length):
				circle_copy[(current_position + i) % circle_size] = circle[(current_position + length - 1 - i) % circle_size]
			circle = circle_copy
			current_position = (current_position + length + skip_size) % circle_size
			skip_size += 1

		return circle, current_position, skip_size
