from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):

		nb_char = 0
		is_garbage = False
		is_mute = False

		for character in s:

			if character == ">" and is_garbage and not is_mute :
				is_garbage = False

			if is_garbage and not is_mute and character != "!":
				nb_char += 1

			if character == "<" and not is_garbage and not is_mute:
				is_garbage = True

			if character == "!" and not is_mute:
				is_mute = True
			else:
				is_mute = False

		return nb_char
