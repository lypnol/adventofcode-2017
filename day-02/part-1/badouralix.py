from submission import Submission


class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		rows = s.split('\n')
		checksum = 0

		for row in rows:
			cells = [int(n) for n in row.split()]
			checksum += max(cells) - min(cells)

		return checksum
