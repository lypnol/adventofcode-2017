from submission import Submission


class LizzarocSubmission(Submission):

	def run(self, s):
		return sum([max([int(i) for i in l.split()]) - min([int(i) for i in l.split()]) for l in s.splitlines()])
