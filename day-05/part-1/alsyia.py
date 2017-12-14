from runners.python import Submission

class AlsyiaSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag

		instructions = [int(item) for item in s.split('\n')]
		maxIdx = len(instructions)
		currentIdx = 0
		steps = 0
		while(0 <= currentIdx < maxIdx):
			jump = instructions[currentIdx]
			instructions[currentIdx] += 1
			currentIdx += jump
			steps += 1
		return steps
