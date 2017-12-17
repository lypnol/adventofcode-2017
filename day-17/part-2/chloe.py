from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		jump = int(s)
		curseur = 0
		result = 0
		for i in range(1, 50000001):
			curseur = (curseur + jump) % i + 1
			if curseur == 1:
				result = i
		return result