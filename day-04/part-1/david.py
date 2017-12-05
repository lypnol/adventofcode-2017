from submission import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here

		return sum((1 if self.is_passphrase_valid(p) else 0) for p in s.split("\n"))

	def is_passphrase_valid(self, passphrase):
		words = []
		for word in passphrase.split():
			if word in words:
				return False

			words.append(word)

		return True

