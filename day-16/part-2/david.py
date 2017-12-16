from runners.python import Submission

class DavidSubmission(Submission):

	def run_moves(self):
		n = self.n
		for move in self.moves:
				if move[0] == 's': # spin move
					offset = int(move[1:])
					self.programs = self.programs[-offset:] + self.programs[:n-offset]

				elif move[0] == 'x': # exchange move
					[i, j] = map(int, move[1:].split('/'))
					self.programs[i], self.programs[j] = self.programs[j], self.programs[i]

				elif move[0] == 'p': # partner move
					a,b = move[1:].split('/')
					i, j = self.programs.index(a), self.programs.index(b)
					self.programs[i], self.programs[j] = self.programs[j], self.programs[i]

				else:
					raise Exception("Unknown move: {}".format(move))

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		self.moves = s.split(',')

		self.programs = [chr(i) for i in range(ord('a'), ord('p')+1)]
		self.n = len(self.programs)


		seen_programs = dict()

		# let's try to find a loop
		k = 1
		BOUND = 1000*1000*1000
		while k <= BOUND:
			self.run_moves()

			str_programs = "".join(self.programs)
			if str_programs in seen_programs:
				# loop between seen_programs[str_programs] and k-th iteration
				break

			else:
				seen_programs[str_programs] = k
				k += 1


		# 1 -> ... -> seen_programs[str_programs] -> .... -> k -> ..... -> BOUND
		str_programs = "".join(self.programs)
		factor = k - seen_programs[str_programs]
		remaining_loops = (BOUND-k) % factor
		for _ in range(remaining_loops):
			self.run_moves()

		return "".join(self.programs)
