from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		test = []
		liste = s.split("\n")
		dico = {}
		counter = 0
		for element in liste:
			dico[element.split(' <-> ')[0]] = set(element.split(' <-> ')[1].split(', '))
		while len(dico.keys()) > 0:
			value = dico.popitem()
			dico[value[0]] = value[1]
			value = value[0]
			groupe = self.find_groups(dico,value)
			if len(groupe) > 0:
				counter += 1
			for element in groupe:
				dico.pop(element)
		return counter


	def find_groups(self, dico, value_initiale):
		groupe = set()
		value = value_initiale
		a_traiter = {value}
		groupe.add(value)

		while len(a_traiter) > 0:
			value = a_traiter.pop()
			nouveaux_a_traiter = set(dico[value]).difference(groupe)
			a_traiter = a_traiter.union(nouveaux_a_traiter)
			groupe = groupe.union(set(dico[value]))
		return groupe
