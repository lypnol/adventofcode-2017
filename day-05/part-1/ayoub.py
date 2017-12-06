from submission import Submission


class AyoubSubmission(Submission):

	def run(self, s):
		instructions = list(map(int, s.split('\n')))
		curr = 0
		steps = 0
		while 0 <= curr < len(instructions):
			last = curr
			curr += instructions[curr]
			instructions[last] += 1
			steps += 1
		return steps

