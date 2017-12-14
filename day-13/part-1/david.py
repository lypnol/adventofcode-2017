from runners.python import Submission

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here

		layers = [tuple(map(int, layer.split(': '))) for layer in s.split('\n')]

		return sum((layer_id*depth if layer_id % (2*(depth-1)) == 0 else 0) for layer_id,depth in layers)
