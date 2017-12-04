from submission import Submission


class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here

		return sum((1 if self.is_valid_passphrase(p) else 0) for p in s.split("\n"))


	def is_valid_passphrase(self, passphrase):
		elements = []
		for word in passphrase.split():
			e = "".join(sorted(list(word)))
			if e in elements:
				return False

			elements.append(e)

		return True


