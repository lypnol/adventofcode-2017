from runners.python import Submission

class CocoSubmission(Submission):

	def run(self, s):
		return sum([int(s[i]) for i in range(len(s)) if s[i] == s[(i+1) % len(s)]])