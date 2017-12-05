from runners.python import Submission


class MathieuSubmission(Submission):

	def run(self, s):
		return sum([max(map(int,line))-min(map(int,line)) for line in map(lambda x:x.split(),s.split('\n'))])

