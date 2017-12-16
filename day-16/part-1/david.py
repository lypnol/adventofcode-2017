from runners.python import Submission

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here


		programs = [chr(i) for i in range(ord('a'), ord('p')+1)]
		n = len(programs)
		for move in s.split(','):
			if move[0] == 's': # spin move
				offset = int(move[1:])
				programs = programs[-offset:] + programs[:n-offset]

			elif move[0] == 'x': # exchange move
				[i, j] = map(int, move[1:].split('/'))
				programs[i], programs[j] = programs[j], programs[i]

			elif move[0] == 'p': # partner move
				a,b = move[1:].split('/')
				i, j = programs.index(a), programs.index(b)
				programs[i], programs[j] = programs[j], programs[i]

			else:
				raise Exception("Unknown move: {}".format(move))

		return "".join(programs)
