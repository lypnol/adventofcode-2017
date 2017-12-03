from submission import Submission


class XavierSubmission(Submission):

	def run(self, s):
		c = 0
		rows = s.split("\n")
		for r in rows:
			t = sorted(list(map(int, r.split("\t"))))
			m = len(t)
			for i in range(m):
				for j in range(i + 1, m):
					if t[i] % t[j] == 0:
						c += t[i] - t[j]
		return c
