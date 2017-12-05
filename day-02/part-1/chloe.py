from submission import Submission


class ChloeSubmission(Submission):

	def run(self, s):
		table_str = [row.split() for row in s.split('\n')]
		table_int = [list(map(int, row)) for row in table_str]
		return sum([max(row) - min(row) for row in table_int])