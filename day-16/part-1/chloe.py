from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		string = list('abcdefghijklmnop')
		choregraphie = s.split(',')
		for mouvement in choregraphie:
			if mouvement[0] == 's':
				longueur_groupe = int(mouvement[1:])
				stringA = string[len(string) - longueur_groupe:]
				stringB = string[: len(string) - longueur_groupe]
				string = stringA + stringB

			if mouvement[0] == 'x':
				position1 = int(mouvement[mouvement.index('x') + 1: mouvement.index('/')])
				position2 = int(mouvement[mouvement.index('/') + 1:])
				exchange = string[position1]
				string[position1] = string[position2]
				string[position2] = exchange

			if mouvement[0] == 'p':
				element1 = mouvement[mouvement.index('p') + 1: mouvement.index('/')]
				element2 = mouvement[mouvement.index('/') + 1:]
				position1 = string.index(element1)
				position2 = string.index(element2)
				partner = string[position1]
				string[position1] = string[position2]
				string[position2] = partner

		return ''.join(string)



if __name__ == '__main__':
	string = list('abcde')
	print(''.join(string))
	choregraphie = ['s1','x3/4','pe/b']
	for mouvement in choregraphie:
		if mouvement[0] == 's':
			longueur_groupe = int(mouvement[1:])
			stringA = string[len(string) - longueur_groupe :]
			stringB = string[: len(string) - longueur_groupe]
			string = stringA + stringB

		if mouvement[0] == 'x':
			position1 = int(mouvement[mouvement.index('x') + 1 : mouvement.index('/')])
			position2 = int(mouvement[mouvement.index('/') + 1 :])
			exchange = string[position1]
			string[position1] = string[position2]
			string[position2] = exchange

		if mouvement[0] == 'p':
			element1 = mouvement[mouvement.index('p') + 1: mouvement.index('/')]
			element2 = mouvement[mouvement.index('/') + 1:]
			position1 = string.index(element1)
			position2 = string.index(element2)
			partner = string[position1]
			string[position1] = string[position2]
			string[position2] = partner

	print(''.join(string))