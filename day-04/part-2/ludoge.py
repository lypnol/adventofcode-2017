from submission import Submission


class LudogeSubmission(Submission):


	def is_valid(self, phrase):
		p = phrase.split()
		for i in range(len(p)):
			for j in range(i+1,len(p)):
				if sorted(p[i])==sorted(p[j]):
					return False
		return True

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		valid_phrases = 0
		for phrase in s.split("\n"):
			if self.is_valid(phrase):
				valid_phrases+=1
		return valid_phrases



