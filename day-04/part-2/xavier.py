from runners.python import Submission


class XavierSubmission(Submission):
	def run(self, s):
		c = 0
		rows = s.split("\n")
		for r in rows:
			t = list(r.split(" "))
			l = len(t)
			for i in range(l):
				t[i] = tuple(sorted(t[i]))
			if l == len(set(t)):
				c += 1
		return c
