from submission import Submission


class LoicSubmission(Submission):

	def run(self, s):
		m = s.split("\n")
		r = []

		for i in range(0, len(m)):
			m[i] = [int(n) for n in m[i].split()]
			m[i].sort(reverse=True)

			l = len(m[i])
			for j in range(0, l):
				for k in range(0, l - j - 1):
					if m[i][j] % m[i][l - k - 1] == 0:
						r.append(m[i][j] / m[i][l - k - 1])

		return int(sum(r))
		pass

