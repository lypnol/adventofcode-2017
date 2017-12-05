from runners.python import Submission


class XpfioSubmission(Submission):
	def fromArrayInt(self, table,separator='\t'):
		rows = table.split('\n')
		output = []
		for row in rows:
			# line = row.split(separator)
			line = row.split()
			line = list(map(lambda x: int(x), line))
			output.append(line)
		return output

	def run(self, s):
		return sum([max(i)-min(i) for i in self.fromArrayInt(s)])

