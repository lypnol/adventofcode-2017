from runners.python import Submission
from collections import deque

class BadouralixSubmission(Submission):

	SIZE = 16

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		index = deque([chr(i + 97) for i in range(self.SIZE)])
		ops = s.split(',')

		for op in ops:
			self.apply(op, index)

		return ''.join(index)

	def apply(self, op, index):
		move = op[0]
		if move == 's':
			arg = int(op[1:])
			index.rotate(arg)
		elif move == 'x':
			args = list(map(int, op[1:].split('/')))
			index[args[0]], index[args[1]] = index[args[1]], index[args[0]]
		elif move == 'p':
			args = list(op[1:].split('/'))
			pos = (index.index(args[0]), index.index(args[1]))
			index[pos[0]], index[pos[1]] = index[pos[1]], index[pos[0]]
		else:
			raise TypeError
