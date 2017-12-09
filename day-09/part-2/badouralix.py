from runners.python import Submission

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		counter = 0
		garbage = False
		skip = False

		for char in s:
			if skip:
				skip = False
			else:
				if char == '!':
					skip = True
				elif char == '>':
					garbage = False
				elif not garbage and char == '<':
					garbage = True
				elif garbage:
					counter += 1

		return counter
