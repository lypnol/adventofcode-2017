from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):

		nb_char = 0
		is_garbage = False
		is_mute = False

		for character in s:

			if not is_mute:

				if character == ">" and is_garbage:
					is_garbage = False

				if character != "!" and is_garbage:
					nb_char += 1

				if character == "<" and not is_garbage:
					is_garbage = True

				if character == "!":
					is_mute = True
			else:
				is_mute = False

		return nb_char
