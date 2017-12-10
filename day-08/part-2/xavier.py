from runners.python import Submission
from collections import defaultdict

class XavierSubmission(Submission):
	def inc_or_dec(self, w, v):
		if w == "inc":
			return int(v)
		else:
			return -1 * int(v)

	def run(self, s):
		s = s.split("\n")
		registers = defaultdict(lambda: 0)
		max_value = 0
		for line in s:
			line = line.split(" ")
			comp = line[5]
			line[6] = int(line[6])
			if comp == "==" and registers[line[4]] == line[6] or comp == ">=" and registers[line[4]] >= line[6] or comp == "<=" and registers[line[4]] <= line[6] or comp == "!=" and registers[line[4]] != line[6] or comp == "<" and registers[line[4]] < line[6] or comp == ">" and registers[line[4]] > line[6]:
				registers[line[0]] += self.inc_or_dec(line[1], line[2])
			if registers[line[0]] > max_value:
				max_value = registers[line[0]]
		return max_value