from submission import Submission


class LizzarocSubmission(Submission):

	def run(self, s):
		return sum([isPassphrase(line) for line in s.splitlines()])
		
def isPassphrase(l):
	words = l.split(' ')
	for i in range(len(words)):
		for j in range(i+1, len(words)):
			if isAnagram(words[i], words[j]):
				print("anagram", words[i], words[j])
				return 0
	return 1

def isAnagram(a, b):
	if len(a) != len(b):
		return False
	la = sorted(list(a))
	lb = sorted(list(b))
	for i in range(len(la)):
		if la[i] != lb[i]:
			return False
	return True