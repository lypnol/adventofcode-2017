from submission import Submission


class LoicSubmission(Submission):

	def run(self, s):
		q4 = -1
		e = -1
		s = int(s)

		while q4 < 0:
			e += 1
			if s <= (2 * e + 1) ** 2:
				q4 = (2 * e + 1) ** 2

		if s <= q4 - 6 * e:
			return abs(s - q4 + 7 * e) + e
		elif s <= q4 - 4 * e:
			return abs(s - q4 + 5 * e) + e
		elif s <= q4 - 2 * e:
			return abs(s - q4 + 3 * e) + e
		else:
			return abs(s - q4 + e) + e

