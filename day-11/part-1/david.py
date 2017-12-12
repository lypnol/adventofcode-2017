from runners.python import Submission

from queue import PriorityQueue
import operator
import math


class DavidSubmission(Submission):
	MOVE_OFFSET = {
		'n': (0,2),
		'ne': (2,1),
		'se': (2,-1),
		's': (0,-2),
		'sw': (-2,-1),
		'nw': (-2,1),
	}

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		path = [self.MOVE_OFFSET[x] for x in s.split(',')]
		n = len(path)

		x = 0
		y = 0

		# go the the dst point
		for o_x, o_y in path:
			x += o_x
			y += o_y

		# we reached the destination point !
		dst = (x, y)

		# A* from the source to the destination
		src = (0, 0)

		q = PriorityQueue()
		q.put((0, [src])) # (dst, pos)

		while True:
			distance, path = q.get()
			pos = path[-1]
			if pos == dst:
				# we reached the destination
				return len(path)-1

			for neighbor in self.neighbors(pos):
				if neighbor not in path:
					q.put((len(path) + self.distance(neighbor, dst), path + [neighbor]))


	def neighbors(self, pos):
		return [tuple(map(operator.add, pos, offset)) for offset in self.MOVE_OFFSET.values()]

	def distance(self, pos1, pos2):
		x1, y1 = pos1
		x2, y2 = pos2
		return math.sqrt((x1-x2)**2 + (y1-y2)**2)




