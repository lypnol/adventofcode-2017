from submission import Submission
from collections import defaultdict


class LoicSubmission(Submission):

	def run(self, s):
		m = defaultdict(dict)
		m[0][0] = 1
		xcur = 0
		ycur = 0
		it = 1
		r = 1
		s = int(s)

		while r < s:
			q4 = -1
			e = -1

			while q4 < 0:
				e = e + 1
				if it <= (2 * e + 1) ** 2:
					q4 = (2 * e + 1) ** 2

			if it < q4 - 6 * e:
				xcur += 1
			elif it < q4 - 4 * e:
				ycur -= 1
			elif it < q4 - 2 * e:
				xcur -= 1
			else:
				ycur += 1
			it += 1

			m[xcur][ycur] = self.partialsum(m, xcur, ycur)
			r = m[xcur][ycur]

		return r


	@staticmethod
	def partialsum(m, xcur, ycur):
		r = 0
		pos = [(xcur + c[0], ycur + c[1]) for c in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]]
		for cpos in pos:
			try:
				r += m[cpos[0]][cpos[1]]
			except Exception:
				r += 0
		return r





