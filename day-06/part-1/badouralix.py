from submission import Submission

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		banks = tuple(int(x) for x in s.split())
		history = set()
		while not self.already_seen(banks, history):
			history.add(banks)
			banks = self.run_cycle(banks)
		return len(history)

	def run_cycle(self, banks):
		banks = list(banks)
		size = len(banks)
		max_value = max(banks)
		max_index = banks.index(max_value)
		banks[max_index] = 0
		for offset in range(1, size+1):
			banks[(max_index + offset) % size] += (max_value // size) + (offset <= max_value % size)
		return tuple(banks)

	def already_seen(self, banks, history):
		return banks in history
