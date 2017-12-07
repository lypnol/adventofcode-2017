from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		piles_info = s.split("\n")
		piles_porteuses = [element for element in piles_info if "->" in element]
		dico = {}
		for element in piles_porteuses:
			candidat_potentiel = element[:element.index(" (")]
			dico[candidat_potentiel] = element[element.index(" ("):]

		for candidat in dico.keys():
			IN = sum(1 for value in dico.values() if candidat in value)
			if IN == 0:
				return candidat
