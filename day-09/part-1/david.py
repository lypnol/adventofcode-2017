from runners.python import Submission

class DavidSubmission(Submission):

	MODE_GROUP = 0
	MODE_GARBAGE = 1

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here

		i = 0

		depth = 0
		score = 0

		mode = self.MODE_GROUP

		while i < len(s):
			c = s[i]

			if c == "!":
				i += 2
				continue

			if mode == self.MODE_GARBAGE and c == ">":
				mode = self.MODE_GROUP

			elif mode == self.MODE_GROUP and c == "<":
				mode = self.MODE_GARBAGE

			elif mode == self.MODE_GROUP and c == "{":
				# new group
				depth += 1

			elif mode == self.MODE_GROUP and c == "}":
				score += depth
				depth -= 1

			i += 1

		return score




