from runners.python import Submission


class XpfioSubmission(Submission):

	def run(self, s):
		return sum([int(s[i]) for i in range(len(s)) if s[i-1] == s[i]])

