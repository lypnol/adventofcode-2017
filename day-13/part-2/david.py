from runners.python import Submission

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		layers = [tuple(map(int, layer.split(': '))) for layer in s.split('\n')]

		offset = 0
		while any(((layer_id+offset) % (2*(depth-1)) == 0) for layer_id,depth in layers):
			offset += 1

		return offset
