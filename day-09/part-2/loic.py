from runners.python import Submission


class LoicSubmission(Submission):

	def run(self, s):
		data = list(s)
		in_garbage = False
		score = 0
		for i in range(0, len(data)):
			if not in_garbage and data[i] == "<":
					in_garbage = True
			elif in_garbage:
				if data[i] == ">":
					in_garbage = False
				elif data[i] == "!":
					data[i + 1] = "0"
					score -= 1
				else:
					score += 1
		return score
