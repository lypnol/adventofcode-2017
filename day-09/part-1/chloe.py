from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):

		increment = 0
		score = 0
		is_garbage = False
		is_mute = False

		for character in s:

			if not is_mute:

				if not is_garbage:

					if character == "<":
						is_garbage = True

					if character == "{" :
						increment += 1
						score += increment

					if character == "}":
						increment -= 1

				else:
					if character == ">":
						is_garbage = False

				if character == "!":
					is_mute = True

			else:
				is_mute = False

		return score
