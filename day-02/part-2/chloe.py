from submission import Submission


class ChloeSubmission(Submission):

	def run(self, s):
		table_str = [row.split() for row in s.split('\n')]
		table_int = [list(map(int, row)) for row in table_str]

		total_sum = 0
		for row in table_int:
			cell = 0
			divider = 0
			while row[cell] % row[divider] != 0 or row[cell] == row[divider] :
				divider += 1
				if divider == len(row):
					divider = 0
					cell += 1
			total_sum += row[cell] // row[divider]

		return total_sum
