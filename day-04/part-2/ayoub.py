from runners.python import Submission


class AyoubSubmission(Submission):

	def are_anagrams(self, a, b):
		if len(a) != len(b): 
			return False
		occurences = [ 0 for i in range(26) ]
		for c in a:
			occurences[ord(c) - ord('a')] += 1
		for c in b:
			occurences[ord(c) - ord('a')] -= 1
		for o in occurences:
			if o != 0:
				return False
		return True

	def run(self, s):
		count = 0
		for line in s.split('\n'):
			words = line.split(' ')
			anagrams = False
			for i in range(len(words)):
				for j in range(i+1, len(words)):
					if self.are_anagrams(words[i], words[j]):
						anagrams = True
						break
				if anagrams: break
			if not anagrams:
				count += 1
		return count

