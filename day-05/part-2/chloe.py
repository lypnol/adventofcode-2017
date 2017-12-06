from submission import Submission

class ChloeSubmission(Submission):

	def run(self, s):
		input = list(map(int, s.split('\n')))
		jump_index = 0
		steps = 0
		while jump_index < len(input) :
			jump = input[jump_index]
			if jump >= 3:
				input[jump_index] -= 1
			else :
				input[jump_index] += 1
			jump_index += jump
			steps +=1
		return steps