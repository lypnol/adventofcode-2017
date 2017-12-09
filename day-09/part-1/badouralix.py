from runners.python import Submission

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		current_value = 0
		result = 0
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
				elif not garbage:
					if char == '{':
						current_value += 1
					elif char == '<':
						garbage = True
					elif char == '}':
						result += current_value
						current_value -= 1
						
		return result