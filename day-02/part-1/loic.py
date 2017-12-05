from submission import Submission


class LoicSubmission(Submission):

	def run(self, s):
		m = s.split("\n")
		r = []
		for i in range(0, len(m)):
			m[i] = [int(n) for n in m[i].split()]
			r.append(max(m[i]) - min(m[i]))
		return sum(r)

