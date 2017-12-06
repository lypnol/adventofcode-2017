from submission import Submission


class XavierSubmission(Submission):
	def reallocate(self, s, n):
		max_index, max_value = max(enumerate(s), key=lambda p: p[1])
		s[max_index] = 0
		for i in range(max_value):
			s[(max_index + 1 + i) % n] += 1

	def run(self, s):
		s = list(map(int, s.split("\t")))
		d = {}
		n = len(s)
		t = tuple(s)
		while t not in d.keys():
			d[t] = 1
			self.reallocate(s, n)
			t = tuple(s)
		return len(d)
