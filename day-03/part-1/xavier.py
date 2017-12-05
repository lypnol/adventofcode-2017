from submission import Submission


class XavierSubmission(Submission):
	@staticmethod
	def get_layer(s):
		i = 1
		v = 1
		while v + i * 8 <= s:
			v += i * 8
			i += 1
		return i

	@staticmethod
	def get_cardinals(layer):
		S = (2 * layer + 1) ** 2 - layer
		W = S - 2 * layer
		N = W - 2 * layer
		E = N - 2 * layer
		return [N, S, E, W]

	def run(self, s):
		s = int(s)
		layer = self.get_layer(s)
		return layer + min([abs(s - k) for k in self.get_cardinals(layer)])
