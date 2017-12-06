from submission import Submission


class ChloeSubmission(Submission):

	def run(self, s):
		input = list(map(int,s.split('\t')))
		steps = 0
		liste_deja_vu = [input]
		deja_vu = False
		while not deja_vu:
			steps += 1
			input = self.allocation(input)
			deja_vu = input in liste_deja_vu
			liste_deja_vu.append(input)
		return steps


	def allocation(self, etat_depart):
		etat_final = etat_depart[:]
		n = len(etat_final)
		pointeur = etat_final.index(max(etat_final))
		a_distribuer = max(etat_final)
		etat_final[pointeur] = 0
		while a_distribuer > 0:
			pointeur += 1
			if pointeur == n:
				pointeur = 0
			etat_final[pointeur] += 1
			a_distribuer -= 1
		return etat_final



