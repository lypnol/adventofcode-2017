from submission import Submission

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		banks = [int(x) for x in s.split()]
		record = tuple(banks)
		history = set()
		while not self.already_seen(record, history):
			history.add(record)
			self.run_cycle(banks)
			record = tuple(banks)
		return len(history)

	def run_cycle(self, banks):
		size = len(banks)
		max_value = max(banks)
		max_index = banks.index(max_value)
		eucl_quo = max_value // size
		eucl_rem = max_value % size
		banks[max_index] = 0
		for offset in range(1, size+1):
			banks[(max_index + offset) % size] += eucl_quo+ (offset <= eucl_rem)

	def already_seen(self, banks, history):
		return banks in history
