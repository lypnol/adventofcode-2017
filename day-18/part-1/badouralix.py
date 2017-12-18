import re
from runners.python import Submission

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		ops = []
		p = re.compile('(?P<instr>\w{3}) (?P<reg>\w)( (?P<arg>[a-z0-9-]*))?', re.MULTILINE)
		for line in p.finditer(s):
			ops.append(line.groupdict())

		env = {}
		index = 0
		while True:
			instr = ops[index]['instr']
			reg_name = ops[index]['reg']
			reg_value = self.get_value(reg_name, env)
			arg = self.get_value(ops[index]['arg'], env)

			if instr == 'snd':
				env['freq'] = reg_value
			elif instr == 'set':
				env[reg_name] = arg
			elif instr == 'add':
				env[reg_name] = env.get(reg_name, 0) + arg
			elif instr == 'mul':
				env[reg_name] = env.get(reg_name, 0) * arg
			elif instr == 'mod':
				env[reg_name] = env.get(reg_name, 0) % arg
			elif instr == 'rcv':
				if reg_value != 0:
					break
			elif instr == 'jgz':
				if reg_value > 0:
					index += arg - 1

			index += 1

		return env['freq']

	def get_value(self, reg, env):
		try:
			return int(reg)
		except:
			pass

		try:
			return int(env[reg])
		except:
			return None
