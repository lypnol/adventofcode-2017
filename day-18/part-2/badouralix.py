import re
from runners.python import Submission
from queue import Queue

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		self.ops = []
		p = re.compile('(?P<instr>\w{3}) (?P<reg>\w)( (?P<arg>[a-z0-9-]*))?', re.MULTILINE)
		for line in p.finditer(s):
			self.ops.append(line.groupdict())

		self.result = 0

		envs = ({'id': 0, 'p': 0}, {'id': 1, 'p': 1})
		queues = (Queue(), Queue())
		deadlock = (False, False)
		indexes = [0, 0]
		while True:
			if deadlock[0] and queues[1].empty() \
					and deadlock[1] and queues[0].empty():
				break
			else:
				deadlock = (self.exec_step(indexes, envs[0], queues), \
							self.exec_step(indexes, envs[1], queues))

		return self.result

	def exec_step(self, indexes, env, queues):
		"""
		Arguments:
			indexes {list of int} -- current indexes
			env {dict} -- current environment of the process
			queue {tuple (Queue, Queue)} -- current queues

		Returns:
			[bool] -- is waiting ?
		"""

		process_id = env['id']
		index = indexes[process_id]
		instr = self.ops[index]['instr']
		reg_name = self.ops[index]['reg']
		reg_value = self.get_value(reg_name, env)
		arg = self.get_value(self.ops[index]['arg'], env)

		if instr == 'snd':
			queues[1 - process_id].put(reg_value)
			if (process_id == 1):
				self.result += 1
		elif instr == 'set':
			env[reg_name] = arg
		elif instr == 'add':
			env[reg_name] = env.get(reg_name, 0) + arg
		elif instr == 'mul':
			env[reg_name] = env.get(reg_name, 0) * arg
		elif instr == 'mod':
			env[reg_name] = env.get(reg_name, 0) % arg
		elif instr == 'rcv':
			if queues[process_id].empty():
				return True
			else:
				env[reg_name] = queues[process_id].get(block=False)
		elif instr == 'jgz':
			if reg_value > 0:
				index += arg - 1

		indexes[process_id] = index + 1

		return False

	def get_value(self, reg, env):
		try:
			return int(reg)
		except:
			pass

		try:
			return int(env[reg])
		except:
			return None
