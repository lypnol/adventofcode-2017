from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		liste = [item for item in range(0, 256)]
		pointeur = 0
		skip_size = 0
		n = len(liste)
		longueurs = list(map(int, s.split(',')))
		for lenght in longueurs:
			subliste = [element for element in liste[pointeur:min(n, lenght + pointeur)] + liste[min(pointeur + lenght - n,0):(pointeur + lenght) % n]]
			subliste.reverse()
			i = pointeur
			for element in subliste:
				liste[i % n] = element
				i += 1
			pointeur = (pointeur + lenght + skip_size) % n
			skip_size += 1
		return liste[0] * liste[1]
