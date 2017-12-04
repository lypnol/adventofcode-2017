from submission import Submission


class LoicSubmission(Submission):

	def run(self, s):
		l = [int(x) for x in str(s)]
		l.append(l[0])
		r = 0
		for i in range(0, len(l) - 1):
			if l[i] == l[i + 1]:
				r += l[i]
		return r
