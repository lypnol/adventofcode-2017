from runners.python import Submission

class AlsyiaSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag

		def findLineResult(line):
			for idx, i in enumerate(line[:-1]):
				for j in line[idx:]:
					print(i, j)
					if (i > j and i % j == 0):
						return i // j
					elif (j > i and j % i == 0):
						return j // i

		lines = s.split('\n')
		intLines = [[int(item) for item in line.split()] for line in lines]

		results = [findLineResult(line) for line in intLines]

		return sum(results)


