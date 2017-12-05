from submission import Submission


class LoicSubmission(Submission):

	def run(self, s):
		lines = s.split("\n")
		r = 0
		for phrase in lines:
			phrase = phrase.split(" ");
			for i in range(0, len(phrase)):
				phrase[i] = "".join(sorted(list(phrase[i])))
			if len(phrase) == len(set(phrase)):
				r += 1
		return r


