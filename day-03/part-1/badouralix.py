from runners.python import Submission


class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		n = int(s)
		square = 1

		while (square * square < n):
			square += 2
		
		offset = (square * square - n) % (square - 1)
		
		return (square // 2) + abs(square // 2 - offset)
