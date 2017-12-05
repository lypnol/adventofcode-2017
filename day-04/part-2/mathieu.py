from submission import Submission


class MathieuSubmission(Submission):

	def run(self, s):
		res = 0
		for line in s.split('\n'):
			is_valid = True
			for word in line.split():
				if list(map(set,line.split())).count(set(word))>1:
					is_valid = False
					break
			res += is_valid
		return res