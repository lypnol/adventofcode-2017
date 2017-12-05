from runners.python import Submission


class AyoubSubmission(Submission):

	def run(self, s):
		res = 0
		for line in s.split('\n'):
			r = list(map(int, line.split()))
			res += max(r) - min(r)
		return res