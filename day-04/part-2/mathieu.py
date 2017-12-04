from submission import Submission


class MathieuSubmission(Submission):

	def run(self, s):
		res = 0
		inputs = [line.split() for line in s.split('\n')]
		for line in inputs:
			valid = True
			for word in line:
				if list(map(set,line)).count(set(word))>1:
					valid = False
			if valid:
				res += 1
		return res