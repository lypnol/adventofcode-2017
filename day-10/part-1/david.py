from runners.python import Submission

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		n = 256
		lst = list(range(n))
		lengths = [int(x) for x in s.split(',')]

		pos = 0 # current position index
		skip_size = 0

		for length in lengths:
			i = pos
			j = (pos+length-1)

			for k in range(length//2):
				tmp = lst[(j-k)%n]
				lst[(j-k)%n] = lst[(i+k)%n]
				lst[(i+k)%n] = tmp

			pos = (pos + length + skip_size) % n
			skip_size += 1

		return lst[0]*lst[1]
