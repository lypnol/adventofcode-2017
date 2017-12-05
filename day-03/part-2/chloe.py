from runners.python import Submission


class ChloeSubmission(Submission):

	def run(self, s):

		x = int(s)

		if x == 1:
			return x, [0, 0]

		liste_points = {}
		# Coordinates of the point build
		coordonnees = [0, 0]
		last_point = 1
		carre = 0

		liste_points[tuple(coordonnees)] = last_point

		while last_point < x:
			carre += 1

			coordonnees[0] += 1
			last_point, liste_points = self.ajout_point(coordonnees, liste_points)

			if last_point > x:
				return last_point

			while coordonnees != [carre, -carre]:

				# Build the next point : up from the the bottom-right corner of the square where x is going to be
				while coordonnees[1] != carre:
					coordonnees[1] += 1

					last_point, liste_points = self.ajout_point(coordonnees, liste_points)

					if last_point > x:
						return last_point

				# Build the next point : left from the the top-right corner of the square where x is going to be
				while coordonnees[0] != -carre:
					coordonnees[0] -= 1
					last_point, liste_points = self.ajout_point(coordonnees, liste_points)

					if last_point > x:
						return last_point

				# Build the next point : down from the the top-left corner of the square where x is going to be
				while coordonnees[1] != -carre:
					coordonnees[1] -= 1
					last_point, liste_points = self.ajout_point(coordonnees, liste_points)

					if last_point > x:
						return last_point

				# Build the next point : right from the the bottom-left corner of the square where x is going to be
				while coordonnees[0] != carre:
					coordonnees[0] += 1

					last_point, liste_points = self.ajout_point(coordonnees, liste_points)

					if last_point > x:
						return last_point


	def ajout_point(self, coordonnees, liste_points):
		"""Build another value in the grid"""
		coordonnees_voisin = self.coordonnees_voisin(coordonnees)

		liste_valeur_voisin = [liste_points[tuple(coor_voisin)] for coor_voisin in coordonnees_voisin if
							   tuple(coor_voisin) in liste_points.keys()]

		last_point = sum(liste_valeur_voisin)
		liste_points[tuple(coordonnees)] = last_point
		return last_point, liste_points


	def coordonnees_voisin(self, coordonnees):
		"""Find the coordinates of the value we want to add"""
		return  [
				[coordonnees[0] + 1, coordonnees[1]],
				[coordonnees[0] + 1, coordonnees[1] + 1],
				[coordonnees[0] + 1, coordonnees[1] - 1],
				[coordonnees[0] - 1, coordonnees[1]],
				[coordonnees[0] - 1, coordonnees[1] + 1],
				[coordonnees[0] - 1, coordonnees[1] - 1],
				[coordonnees[0], coordonnees[1] - 1],
				[coordonnees[0], coordonnees[1] + 1],
				]