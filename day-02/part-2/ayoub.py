from submission import Submission


class AyoubSubmission(Submission):

	def run(self, s):
		res = 0
		for line in s.split('\n'):
			r = list(map(int, line.split()))
			found = False
			for i, x in enumerate(r):
				for j, y in enumerate(r):
					if i != j and x % y == 0:
						res += x // y
						found = True
						break
				if found: break
		return res