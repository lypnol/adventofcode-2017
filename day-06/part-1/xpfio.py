from runners.python import Submission
import math
from itertools import groupby
import operator

class XpfioSubmission(Submission):

	def run(self, s):

		banks = s.split('\t')
		banks = list(map(lambda x: int(x), banks))

		positions = []
		steps = 0

		while banks not in positions:
			# print(banks)
			positions.append(banks.copy())
			steps += 1
			index, value = max(enumerate(banks), key=operator.itemgetter(1))
			banks[index] = 0
			while value >= 1:
				index += 1
				index %= len(banks)
				banks[index] += 1
				value -= 1

		return steps