from submission import Submission


class XavierSubmission(Submission):

	def run(self, s):
		c = 0
		rows = s.split("\n")
		for r in rows:
			t = sorted(list(map(int, r.split("\t"))))
			c += t[-1] - t[0]
		return c