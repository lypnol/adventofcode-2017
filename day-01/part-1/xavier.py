from submission import Submission


class XavierSubmission(Submission):

	def run(self, s):
		k = len(s)
		return sum(int(s[i]) for i in range(k) if s[i] == s[(i+1) % k])
