from runners.python import Submission


class MathieuSubmission(Submission):
	def run(self, s):
		count = 0
		in_garbage = False
		exclamation_before = False
		for char in s:
			if in_garbage:
				if exclamation_before:
					exclamation_before = False
				elif char == "!":
					exclamation_before = True
				else:
					if char == ">":
						in_garbage = False
					else:
						count += 1
			elif char == "<":
				in_garbage = True
		return count

