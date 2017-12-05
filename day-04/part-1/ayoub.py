from submission import Submission


class AyoubSubmission(Submission):

	def run(self, s):
		count = 0
		for line in s.split('\n'):
			words = line.split(' ')
			if len(set(words)) == len(words):
				count += 1
		return count

