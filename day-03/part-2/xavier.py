from runners.python import Submission


class XavierSubmission(Submission):
	@staticmethod
	def get_next_position(p):
		"""
		Thanks @badouralix !
		"""
		x = p[0]
		y = p[1]

		if x + y <= 0 <= x - y:
			return x + 1, y
		elif x + y >= 0 and x - y > 0:
			return x, y + 1
		elif x + y > 0 >= x - y:
			return x - 1, y
		elif x + y <= 0 and x - y < 0:
			return x, y - 1

	@staticmethod
	def get_neighbours(p):
		return [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1), (p[0] + 1, p[1] + 1)] \
				+ [(p[0] - 1, p[1] - 1), (p[0] + 1, p[1] - 1), (p[0] - 1, p[1] + 1)]

	def run(self, s):
		s = int(s)
		spiral = {(0, 0): 1}
		cur_pos = (0, 0)
		while spiral[cur_pos] < s:
			cur_pos = self.get_next_position(cur_pos)
			spiral[cur_pos] = sum([spiral.get(k, 0) for k in self.get_neighbours(cur_pos)])
		return spiral[cur_pos]
