from runners.python import Submission


class XpfioSubmission(Submission):

	def run(self, s):
		n = len(s)
		return sum([int(s[i]) for i in range(n) if s[i] == s[(i+n//2) % n]])

