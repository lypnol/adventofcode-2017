from runners.python import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		t = [int(x) for x in s.split("\n")]
		n = len(t)
		i = 0

		steps = 0

		while 0 <= i < n:
			before = i
			i += t[i]
			if t[before] >= 3:
				t[before] -= 1
			else:
				t[before] += 1
			steps += 1

		return steps
