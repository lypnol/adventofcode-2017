from submission import Submission


class ChloeSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		variable = s + s[0]
		total_sum = 0

		for digit_index in range(len(s)):
			if variable[digit_index] == variable[digit_index + 1]:
				total_sum += int(variable[digit_index])

		return total_sum
