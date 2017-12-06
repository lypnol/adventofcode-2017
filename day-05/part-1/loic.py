from submission import Submission


class LoicSubmission(Submission):

	def run(self, s):
		data = [int(x) for x in s.split("\n")]
		r = 0
		i = 0

		while i < len(data):
			r += 1
			data[i] += 1
			i += data[i] - 1

		return r

