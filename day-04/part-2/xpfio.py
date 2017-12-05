from submission import Submission


class XpfioSubmission(Submission):

	def run(self, s):
		return sum([1 \
				for line in s.split('\n') \
				if len(set(map(lambda x:''.join(sorted(x)),line.split(' ')))) == len(line.split(' ')) ])