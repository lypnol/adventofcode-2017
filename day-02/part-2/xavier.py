from submission import Submission


class XavierSubmission(Submission):

	def get_dividers(self,r):
		t = sorted(list(map(int, r.split("\t"))), reverse=True)
		for i in range(len(t)):
			for j in range(i + 1, len(t)):
				if t[i] % t[j] == 0:
					return [t[i], t[j]]

	def run(self, s):
		c = 0
		rs = s.split("\n")
		for r in rs:
			t = self.get_dividers(r)
			c += t[0] // t[1]
		return c
