from submission import Submission


class XpfioSubmission(Submission):

	def fromArrayInt(self, table,separator='\t'):
		rows = table.split('\n')
		output = []
		for row in rows:
			line = row.split()
			# line = row.split(separator)
			line = list(map(lambda x: int(x), line))
			output.append(line)
		return output

	def run(self, s):
		arr = self.fromArrayInt(s)
		return sum([max([x//y for x in line for y in line if x%y==0]) for line in arr])
