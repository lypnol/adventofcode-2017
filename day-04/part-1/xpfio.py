from runners.python import Submission


class XpfioSubmission(Submission):

	def run(self, s):
		return sum([1 \
				for line in s.split('\n') \
				if len(set(line.split(' '))) == len(line.split(' ')) ])
