from runners.python import Submission


class XpfioSubmission(Submission):

	def run(self, s):
		row = s.split('\n')
		row = list(map(lambda x: int(x), row))

		steps = 0 
		position = 0
		while position >= 0 and position < len(row):
			current = row[position]
			if current >= 3:
				row[position] -= 1
			else:
				row[position] +=1
				
			position += current
			steps +=1
		
		return steps
