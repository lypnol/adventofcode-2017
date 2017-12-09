from runners.python import Submission


class AyoubSubmission(Submission):

	def run(self, s):
		total_score = 0
		current_score = 0
		ignored = False
		inside_garbage = False
		for c in s:
			if ignored:
				ignored = False
				continue
			if inside_garbage and c != '>':
				if c == '!':
					ignored = True
				continue
			if inside_garbage and c == '>':
				inside_garbage = False
			elif c == '{':
				current_score += 1
			elif c == '}':
				total_score += current_score
				current_score -= 1
			elif c == '<':
				inside_garbage = True

		return total_score