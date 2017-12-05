from runners.python import Submission


class LoicSubmission(Submission):

	def run(self, s):
		l = [int(x) for x in str(s)]
		k = int(len(l) / 2)
		l += l
		r = 0
		for i in range(0, 2 * k):
			if l[i] == l[i + k]:
				r += l[i]
		return r
