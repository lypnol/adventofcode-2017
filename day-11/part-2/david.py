from runners.python import Submission

from queue import PriorityQueue
import operator
import math

class DavidSubmission(Submission):
	MOVE_OFFSET = {
		'n':  ( 0, 1,-1),
		'ne': ( 1, 0,-1),
		'se': ( 1,-1, 0),
		's':  ( 0,-1, 1),
		'sw': (-1, 0, 1),
		'nw': (-1, 1, 0),
	}

	def run(self, s):

		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		moves = [self.MOVE_OFFSET[x] for x in s.split(',')]

		src = (0,0,0)
		path = [src]

		for move in moves:
			next_pos = self.sum_vectors(path[-1], move)
			path.append(next_pos)

		return max(self.distance(pos) for pos in path)

	def sum_vectors(self, v1, v2):
		return tuple(map(operator.add, v1, v2))

	def distance (self, pos):
		return max((abs(x) for x in pos))





