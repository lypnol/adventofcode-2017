from runners.python import Submission

class AlsyiaSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag

		instructions = [int(item) for item in s.split('\n')]

		currentIdx = 0
		steps = 0
		while True:
			try:
				jump = instructions[currentIdx]
				instructions[currentIdx] += -1 if jump >= 3 else 1
				currentIdx += jump
				steps += 1
			except IndexError:
				return steps

