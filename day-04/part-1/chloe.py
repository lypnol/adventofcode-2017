from submission import Submission


class ChloeSubmission(Submission):

	def run(self, s):
		liste_passphrase = s.split("\n")
		return sum(1 for passphrase in liste_passphrase if self.is_valid(passphrase))


	def is_valid(self, passphrase):
		mots = passphrase.split(" ")
		valide = True
		for mot in mots:
			if mots.count(mot) > 1:
				valide = False
				break
		return valide