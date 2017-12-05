from runners.python import Submission


class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		rows = s.split('\n')
		checksum = 0

		for row in rows:
			cells = [int(n) for n in row.split()]
			for i in range(len(cells)):
				for j in range(i+1, len(cells)):
					maxi = max(cells[i], cells[j])
					mini = min(cells[i], cells[j])
					if maxi % mini == 0:
						checksum += maxi // mini
						break
				else:
					continue
				break

		return checksum

