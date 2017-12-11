from runners.python import Submission
import fibonacci_heap_mod as hq


class AyoubSubmission(Submission):

	direction = {
		'ne': (1, 0),
		'n': (1, -1),
		'nw': (0, -1),
		'sw': (-1, 0),
		's': (-1, 1),
		'se': (0, 1)
	}

	# Using https://www.redblobgames.com/grids/hexagons/#coordinates-cube
	def run(self, s):
		q, r = 0, 0
		max_dist = 0
		for move in s.split(','):
			u, v = self.direction[move]
			q, r = q+u, r+v
			x, y, z = q, r, -q-r
			dist = (abs(x) + abs(y) + abs(z)) // 2
			max_dist = max(max_dist, dist)
		return max_dist