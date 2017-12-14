from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		liste = s.split('\n')
		dico = {}
		for element in liste:
			dico[int(element.split(': ')[0])] = int(element.split(': ')[1])
		waiting_time = 0
		spotted = True
		while spotted:
			waiting_time += 1
			spotted = False
			for layer in dico.keys():
				if (layer + waiting_time) % ((dico[layer] - 1) * 2) == 0:
					spotted = True
					break
		return waiting_time
