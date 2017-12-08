from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		input = s.split("\n")
		piles_portantes = [element for element in input if "->" in element]
		dico ={}

		for element in piles_portantes:
			candidat_potentiel = element[:element.index(" (")]
			dico[candidat_potentiel] = element[element.index(" ("):]
		for candidat in dico.keys():
			test_in = sum(1 for value in dico.values() if candidat in value)
			if test_in == 0:
				return candidat
