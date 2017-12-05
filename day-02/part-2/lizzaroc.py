from submission import Submission


class LizzarocSubmission(Submission):

	def run(self, s):
		lines = s.splitlines()
		return sum(map(self.getQuotient, lines))
	
	def getQuotient(self, l):
		intl = list(map(int, l.split()))
		for idx, i in enumerate(intl):
			for idxj in range(idx + 1, len(intl)):
				j = intl[idxj]
				if i % j == 0:
					return i//j
				elif j % i == 0:
					return j//i