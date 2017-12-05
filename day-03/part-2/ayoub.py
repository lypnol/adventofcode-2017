from submission import Submission
from itertools import product


class AyoubSubmission(Submission):

	def add_layer(self, m):
		n = len(m) + 2
		p = [[None for j in range(n)] for i in range(n)]
		for i in range(n-2):
			for j in range(n-2):
				p[i+1][j+1] = m[i][j]
		return p

	def put_sum_value(self, m, i, j):
		n = len(m)
		s = 0
		for (u, v) in product([-1, 0, 1], repeat=2):
			if (u, v) == (0, 0): continue
			if i+u < 0 or i+u >= n: continue
			if j+v < 0 or j+v >= n: continue
			if m[i+u][j+v] is None: continue
			s += m[i+u][j+v]
		m[i][j] = s
		return s

	def run(self, s):
		x = int(s)
		n = 1
		m = [[1]]
		i, j = 0, 0
		v = 1
		while v < x:
			if (i, j) == (n-1, n-1):
				m = self.add_layer(m)
				n += 2
				i, j = n-2, n-1
			elif j == n-1 and i > 0:
				i -= 1
			elif i == 0 and j > 0:
				j -= 1
			elif j == 0 and i < n-1:
				i += 1
			elif i == n-1 and j < n-1:
				j += 1 

			v = self.put_sum_value(m, i, j)
		return v