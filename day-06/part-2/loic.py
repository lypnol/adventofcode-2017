from submission import Submission

class LoicSubmission(Submission):

	def run(self, s):
		d = [int(x) for x in s.split("\t")]
		t = {}
		compteur = 0

		while tuple(d) not in t.keys():
			t[tuple(d)] = compteur
			compteur += 1

			buffer = max(d)
			i = d.index(buffer)
			d = self.data_update(d, i)

		return compteur - t[tuple(d)]

	def data_update(self, d, i):
		c = d[i]
		d[i] = 0
		for k in range(0, c):
			i = (i + 1) % 16
			d[i] += 1
		return d