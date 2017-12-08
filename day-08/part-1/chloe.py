from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		instructions = s.split('\n')
		registres = {}
		for line in instructions:
			registreop = line.split(" if ")[0].split()[0]
			operation = line.split(" if ")[0].split()[1]
			modification = int(line.split(" if ")[0].split()[2])

			registrecond = line.split(" if ")[1].split()[0]
			test = line.split(" if ")[1].split()[1]
			valeur_condition = int(line.split(" if ")[1].split()[2])

			if registrecond not in registres.keys():
				registres[registrecond] = 0
			if registreop not in registres.keys():
				registres[registreop] = 0

			if test == '>':
				condition = registres[registrecond] > valeur_condition
			if test == '>=':
				condition = registres[registrecond] >= valeur_condition
			if test == '<':
				condition = registres[registrecond] < valeur_condition
			if test == '<=':
				condition = registres[registrecond] <= valeur_condition
			if test == '==':
				condition = registres[registrecond] == valeur_condition
			if test == '!=':
				condition = registres[registrecond] != valeur_condition

			if condition:
				if "inc" in operation:
					registres[registreop] += modification
				if 'dec' in operation:
					registres[registreop] -= modification
		return max(registres.values())




