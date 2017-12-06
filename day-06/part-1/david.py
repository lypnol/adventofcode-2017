from submission import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		distrib = [int(x) for x in s.split()]
		n = len(distrib)

		seen_distribs = set()

		counter = 0

		while tuple(distrib) not in seen_distribs:
			counter += 1
			seen_distribs.add(tuple(distrib))

			i = max(range(n), key=lambda x: distrib[x])
			blocks = distrib[i]
			distrib[i] = 0
			for j in range(1, blocks+1):
				distrib[(i+j) % n] += 1

		return counter





