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
				if s[p] >= 3:
					s[p] -= 1
				else:
					s[p] += 1
				p = next
			except IndexError:
				return c - 1
