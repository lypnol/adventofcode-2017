from submission import Submission


class XavierSubmission(Submission):
	def run(self, s):
		s = list(map(int, s.split("\n")))
		p = 0
		c = 0
		while True:
			try:
				c += 1
				s[p] += 1
				p += s[p] - 1
			except:
				return c - 1

