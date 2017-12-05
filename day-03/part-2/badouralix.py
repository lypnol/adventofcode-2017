from submission import Submission


class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		n = int(s)
		position = (0,0)
		value = 1
		spiral = {position: value}

		while (value < n):
			position = self.update_position(position)
			value = sum([spiral.get(neighbor, 0) for neighbor in self.neighbors(position)])
			spiral[position] = value
		
		return value

	def update_position(self, pos):
		x = pos[0]
		y = pos[1]

		if x + y <= 0 and x - y >= 0:
			return (x + 1, y)
		elif x + y >= 0 and x - y > 0:
			return (x, y + 1)
		elif x + y > 0 and x - y <= 0:
			return (x - 1, y)
		elif x + y <= 0 and x - y < 0:
			return (x, y - 1)

	def neighbors(self, pos):
		neighbors = []
		for i in range(-1,2):
			for j in range(-1,2):
				if i != 0 or j != 0:
					neighbors.append((pos[0]-i, pos[1]-j))
		return neighbors
