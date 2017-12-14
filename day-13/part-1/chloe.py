from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		liste = s.split('\n')
		dico = {}
		severity = 0
		for element in liste:
			dico[int(element.split(': ')[0])] = int(element.split(': ')[1])
		for layer in dico.keys():
			if layer % ((dico[layer] - 1) * 2) == 0:
				severity += layer * dico[layer]
		return severity