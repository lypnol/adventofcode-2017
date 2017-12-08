from submission import Submission


class LoicSubmission(Submission):
	memory = {}

	def run(self, s):
		self.memory = {}
		for line in s.split("\n"):
			data = line.split()
			check = False

			if data[5] == "<":
				if self.get(data[4]) < int(data[6]):
					check = True
			elif data[5] == ">":
				if self.get(data[4]) > int(data[6]):
					check = True
			elif data[5] == "<=":
				if self.get(data[4]) <= int(data[6]):
					check = True
			elif data[5] == ">=":
				if self.get(data[4]) >= int(data[6]):
					check = True
			elif data[5] == "==":
				if self.get(data[4]) == int(data[6]):
					check = True
			else:
				if self.get(data[4]) != int(data[6]):
					check = True

			if check:
				if data[1] == "inc":
					self.memory[data[0]] = self.get(data[0]) + int(data[2])
				else:
					self.memory[data[0]] = self.get(data[0]) - int(data[2])

		return max(self.memory.values())

	def get(self, key):
		if key not in self.memory:
			self.memory[key] = 0
			return 0
		return self.memory[key]
