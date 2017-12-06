from submission import Submission


class XavierSubmission(Submission):
	def run(self, s):
		s = list(map(int, s.split("\n")))
		p = 0
		c = 0
		while True:
			try:
				c += 1
				next = p + s[p]
				s[p] += 1 if s[p] < 3 else -1
				p = next
			except:
				return c - 1
