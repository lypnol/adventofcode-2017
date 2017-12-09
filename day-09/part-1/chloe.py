from runners.python import Submission

class ChloeSubmission(Submission):

	def run(self, s):

		increment = 0
		score = 0
		is_garbage = False
		is_mute = False

		for character in s:

			if character == "<" and not is_garbage and not is_mute:
				is_garbage = True

			if character == ">" and is_garbage and not is_mute :
				is_garbage = False

			if character == "{" and not is_garbage and not is_mute:
				increment += 1
				score += increment

			if character == "}" and not is_garbage and not is_mute:
				increment -= 1

			if character == "!" and not is_mute:
				is_mute = True
			else:
				is_mute = False

		return score
