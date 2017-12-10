from runners.python import Submission


class AyoubSubmission(Submission):

	def run(self, s):
		non_ignored = 0
		ignored = False
		inside_garbage = False
		for c in s:
			if ignored:
				ignored = False
				continue				
			if inside_garbage and c != '>':
				if c == '!':
					ignored = True
				else:
					non_ignored += 1
				continue
			if inside_garbage and c == '>':
				inside_garbage = False
			elif c == '<':
				inside_garbage = True

		return non_ignored