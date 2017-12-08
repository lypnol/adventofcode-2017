from runners.python import Submission

from collections import defaultdict

class DavidSubmission(Submission):
	COMP_OPERATORS = {
		'==': '__eq__',
		'!=': '__ne__',
		'<=': '__le__',
		'<':  '__lt__',
		'>=': '__ge__',
		'>':  '__gt__',
	}

	OPERATORS = {
		'inc': '__add__',
		'dec': '__sub__',
	}

	def __init__(self):
		super().__init__()
		self.register = defaultdict(int)

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here

		for line in s.split("\n"):
			var, op, value, cond_var, cond_type, cond_value = self.process_line(line)
			if self.compare(cond_var, cond_type, cond_value):
				self.compute(var, op, value)

		return max(self.register.values())

	def compare(self, cond_var, cond_type, cond_value):
		op = self.COMP_OPERATORS[cond_type]
		return getattr(self.register[cond_var], op)(cond_value)

	def compute(self, var, op_type, value):
		op = self.OPERATORS[op_type]
		self.register[var] = getattr(self.register[var], op)(value)

	def process_line(self, line):
		pieces = line.split(" ")
		[var, operation, value, _, condition_var, condition_type, condition_value] = pieces
		assert operation in ['inc', 'dec']
		value = int(value)
		assert condition_type in self.COMP_OPERATORS.keys()
		condition_value = int(condition_value)

		return (var, operation, value, condition_var, condition_type, condition_value)
