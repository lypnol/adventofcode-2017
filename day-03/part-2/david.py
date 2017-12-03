from submission import Submission


class DavidSubmission(Submission):
	UP = 0
	LEFT = 1
	DOWN = 2
	RIGHT = 3

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here

		limit = int(s)

		table = dict()
		table[(0,0)] = 1

		pos = (1,0)
		table[pos] = 1
		direction = self.UP


		while table[pos] <= limit:
			next_pos = self.find_next_position(pos, direction)
			if len(self.neighbors(table, next_pos)) <= 1:
				# no neighbors enough, need to change direction
				direction = (direction+1) % 4
				next_pos = self.find_next_position(pos, direction)


			table[next_pos] = sum([table[p] for p in self.neighbors(table, next_pos)])
			self.debug("table[{}] = {}".format(next_pos, table[next_pos]))
			pos = next_pos

		return table[pos]


	def find_next_position(self, pos, direction):
		x, y = pos

		if direction == self.UP:    return (x, y+1)
		if direction == self.LEFT:  return (x-1, y)
		if direction == self.DOWN:  return (x, y-1)
		if direction == self.RIGHT: return (x+1, y)

	def neighbors(self, table, pos):
		x, y = pos
		adjacent_pos = [(x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1)]
		return [p for p in adjacent_pos if p in table]



