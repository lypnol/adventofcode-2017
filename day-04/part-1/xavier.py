from submission import Submission


class XavierSubmission(Submission):

	def run(self, s):
		c = 0
		rows = s.split("\n")
		for r in rows:
			t = list(r.split(" "))
			if len(t) == len(set(t)):
				c += 1
		return c
