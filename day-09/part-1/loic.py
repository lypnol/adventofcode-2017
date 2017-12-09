from runners.python import Submission


class LoicSubmission(Submission):

	def run(self, s):
		data = list(s)
		in_garbage = False
		score = 0
		level = 0
		for i in range(0, len(data)):
			if not in_garbage:
				if data[i] == "{":
					level += 1
					score += level
				elif data[i] == "}":
					level -= 1
				elif data[i] == "<":
					in_garbage = True
			else:
				if data[i] == "!":
					data[i + 1] = "0"
				if data[i] == ">":
					in_garbage = False
		return score
