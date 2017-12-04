from submission import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here

		# assert(self.spiral(1) == (0,1,1))
		# assert(self.spiral(2) == (1,2,3))
		# assert(self.spiral(9) == (1,2,3))
		# assert(self.spiral(10) == (2,10,5))
		# assert(self.spiral(25) == (2,10,5))

		# find elements on the spiral with minimum distance
		# assert(self.find_min_elements(1,2,3) == [2,4,6,8])
		# assert(self.find_min_elements(2,10,5) == [11,15,19,23])

		e = int(s)
		n, start, h = self.spiral(e)

		min_elements = self.find_min_elements(n, start, h)

		# find distance to the closest min element
		min_distance = min((abs(min_e - e)) for min_e in min_elements)

		return n + min_distance


	def spiral(self, e):
		"""
			Returns in which spiral is an integer e
			A spiral is identified by its length, start position and height

			example: spiral(1) = (0, 1, 1)
			         spiral(2) = (1, 2, 3)
					 spiral(9) = (1, 2, 3)
					 spiral(10) = (2, 10, 5)
					 spiral(25) = (2, 25, 5)
		"""
		if e == 1:
			return (0, 1, 1)

		spiral_n = 1 # n
		spiral_start = 2 # u(n)

		while True:
			next_spiral_start = spiral_start + 8 * spiral_n
			if e < next_spiral_start:
				return (spiral_n, spiral_start, 2*spiral_n + 1)
			else:
				spiral_n += 1
				spiral_start = next_spiral_start


	def find_min_elements(self, n, start, h):
		return [(start + n-1 + 2*n*k) for k in range(4)]


