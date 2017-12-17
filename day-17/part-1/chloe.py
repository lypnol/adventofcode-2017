from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		jump = int(s)
		curseur = 0
		liste = [0]
		for i in range(1, 2018):
			position_insertion = (curseur + jump + 1) % len(liste)
			liste.insert(position_insertion, i)
			curseur = position_insertion
		return liste[liste.index(2017) + 1]