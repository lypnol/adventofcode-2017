from submission import Submission


class LudogeSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		offsets = [int(x) for x in s.split()]
		i=0
		steps=0
		while True:
			oldoffset = offsets[i]
			if offsets[i]>=3:
				offsets[i]-=1
			else:
				offsets[i]+=1
			if i+offsets[i]-1>=len(offsets):
				return steps
			else:
				i+=oldoffset
				steps+=1
		pass

