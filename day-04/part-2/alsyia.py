from runners.python import Submission
from collections import Counter

class AlsyiaSubmission(Submission):

	def checkPassphrase(self, listOfWords):
		# for idx, word in enumerate(listOfWords):
		# 	for i in range(idx+1, len(listOfWords)):
		# 		if sorted(word) == sorted(listOfWords[i]):
		# 			return False
		# return True
		alreadySeen = []

		for word in listOfWords:
				if sorted(word) in alreadySeen:
					return False
				else:
					alreadySeen.append(sorted(word))
		return True


	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		lines = s.split('\n')

		wordsLines = [line.split(' ') for line in lines]
		i = 0
		for listOfWords in wordsLines:
			if(self.checkPassphrase(listOfWords)):
				i += 1
		return i

