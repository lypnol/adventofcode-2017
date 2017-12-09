from runners.python import Submission
from collections import defaultdict
import re

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		registers = defaultdict(int)
		global_max = 0
		regex = (
			'(?P<reg>\w+)',
			'(?P<op>(inc|dec))',
			'(?P<val>[-+]?\d+)',
			'if',
			'(?P<cond_reg>\w+)',
			'(?P<cond_comp>(==|!=|<|<=|>|>=))',
			'(?P<cond_val>[-+]?\d+)',
		)
		p = re.compile('\s'.join(regex), re.MULTILINE)
		for line in p.finditer(s):
			instr = line.groupdict()
			if self.check_cond(instr['cond_reg'], instr['cond_comp'], instr['cond_val'], registers):
				global_max = max(global_max, self.update_reg(instr['reg'], instr['op'], instr['val'], registers))
		return global_max

	def check_cond(self, cond_reg, cond_comp, cond_val, registers):
		reg_val = registers[cond_reg]
		comp_val = int(cond_val)

		if cond_comp == '==':
			return reg_val == comp_val
		elif cond_comp == '!=':
			return reg_val != comp_val
		elif cond_comp == '<':
			return reg_val < comp_val
		elif cond_comp == '<=':
			return reg_val <= comp_val
		elif cond_comp == '>':
			return reg_val > comp_val
		elif cond_comp == '>=':
			return reg_val >= comp_val
		else:
			raise NotImplementedError

	def update_reg(self, reg, op, val, registers):
		val = int(val)

		if op == 'inc':
			registers[reg] += val
		elif op == 'dec':
			registers[reg] -= val
		else:
			raise NotImplementedError

		return registers[reg]
