from submission import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		liste_passphrase = s.split("\n")
		return sum(1 for passphrase in liste_passphrase if self.is_valid(passphrase))


	def is_anagramme(self, mot1, mot2):
		motord1 = "".join(sorted(mot1))
		motord2 = "".join(sorted(mot2))
		return motord1 == motord2


	def is_valid(self, passphrase):
		mots = passphrase.split(" ")
		valide = True
		for mot in mots:
			anagramme_compteur = 0
			for j in range(len(mots)):
				if self.is_anagramme(mot,mots[j]):
					anagramme_compteur += 1
			if anagramme_compteur > 1:
				valide = False
				break
		return valide