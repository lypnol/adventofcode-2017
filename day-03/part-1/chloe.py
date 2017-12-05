from runners.python import Submission


class ChloeSubmission(Submission):

	def run(self, s):
		"""
		Manhattan distance is compute :
		d(point, 1) = | point(abscisse) | + | point(ordonnee) |
		"""
		value = int(s)
		return sum(list(map(abs, self.position_chiffre(value))))


	def point_bottom_right(self, x):
		"""
		:param x: input in a int format

		:return:
		1. the number in the bottom-right corner in the last square drawn before starting the one where x will be
		2. the number of squares drawn before (the 'perimeter' of the previous square)
		"""

		# The number of numbers that are going to be added in the next square increase of 8 at every square
		# (8 numbers added for the 1st square, 16 numbers added for the 2nd square, 24 numbers added for the 3rd square,...)
		nb_add_layer = 0

		# Number in the bottom-right corner
		last_number = 1

		# Number of squares drawn
		layer = 0

		while x > last_number:
			layer +=1
			nb_add_layer += 8
			last_number += nb_add_layer
		return (last_number - nb_add_layer), layer



	def position_chiffre(self, x):
		"""
		Computes the coordinates of the input in the graph where 1 = (0, 0)
		Manhattan distance is compute d(point, 1) = |point(abscisse)|  + |point(ordonnee)|
		"""

		if x== 1:
			return [0,0]

		last_point, carre = self.point_bottom_right(x)

		# Coordinates of the bottom-right corner of the square where x is going to be
		coordonnees = [carre, -carre]

		# Build the last square : up from the the bottom-right corner of the square where x is going to be
		while coordonnees[1] != carre:
			coordonnees[1] += 1
			last_point += 1
			if last_point == x:
				return coordonnees

		# Build the last square : left from the the top-right corner of the square where x is going to be
		while coordonnees[0] != -carre:
			coordonnees[0] -= 1
			last_point += 1
			if last_point == x:
				return coordonnees

		# Build the last square : down from the the top-left corner of the square where x is going to be
		while coordonnees[1] != -carre:
			coordonnees[1] -= 1
			last_point += 1
			if last_point == x:
				return coordonnees

		# Build the last square : right from the the bottom-left corner of the square where x is going to be
		while coordonnees[0] != carre:
			coordonnees[0] += 1
			last_point += 1
			if last_point == x:
				return coordonnees