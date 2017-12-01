from submission import Submission


class AyoubSubmission(Submission):

	def run(self, s):
		s = list(map(int, list(s)))
		n = len(s)
		r = 0
		for i in range(n):
			if s[i] == s[(i+1) % n]:
				r += s[i]
		return r
