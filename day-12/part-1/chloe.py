from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		liste = s.split("\n")
		dico = {}
		groupe = set()
		for element in liste:
			dico[element.split(' <-> ')[0]] = set(element.split(' <-> ')[1].split(', '))
		value = '0'
		a_traiter = {'0'}
		groupe.add(value)

		while len(a_traiter) > 0:
			value = a_traiter.pop()
			nouveaux_a_traiter = set(dico[value]).difference(groupe)
			a_traiter = a_traiter.union(nouveaux_a_traiter)
			groupe = groupe.union(set(dico[value]))
		return(len(groupe))

