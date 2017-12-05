from submission import Submission


class LizzarocSubmission(Submission):

	def run(self, s):
		return sum([isPassphrase(line) for line in s.splitlines()])
		
def isPassphrase(l):
	words = l.split(' ')
	result = 1
	for i in range(len(words)):
		for j in range(i+1, len(words)):
			if words[i] == words[j]:
				return 0
	return result


