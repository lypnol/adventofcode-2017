from runners.python import Submission
import operator
from functools import reduce
from collections import defaultdict

class DavidSubmission(Submission):

	def compute_hash(self, value):
		n = 256
		lst = list(range(n))
		lenghts = [ord(x) for x in value] + [17, 31, 73, 47, 23]

		pos = 0 # current position index
		skip_size = 0

		# 64 rounds
		for _ in range(64):
			for length in lenghts:
				i,j = (pos, pos+length-1)

				for k in range(length//2):
					# swap lst[(j-k)%n] and lst[(i+k)%n]
					lst[(j-k)%n], lst[(i+k)%n] = lst[(i+k)%n], lst[(j-k)%n]

				pos = (pos + length + skip_size) % n
				skip_size += 1

		def xor(l):
			return reduce(operator.xor, l, 0)

		return "".join(["{0:08b}".format(x) for x in [xor(lst[16*k:16*(k+1)]) for k in range(16)]])


	def neighbors(self, pos):
		x,y = pos
		return [p for p in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]]


	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here

		graph = defaultdict(set)
		hashes = [self.compute_hash("{}-{}".format(s, str(i))) for i in range(128)]
		to_visit = set()
		for i, bits in enumerate(hashes):
			for j, b in enumerate(bits):
				node = (i,j)
				if b == "1":
					to_visit.add(node)
					for neighbor in self.neighbors(node):
						graph[neighbor].add(node)

		counter = 0

		while to_visit:
			counter += 1
			root = to_visit.pop()
			to_visit_in_region = [root]

			while to_visit_in_region:
				e = to_visit_in_region.pop()
				if e in to_visit: to_visit.remove(e)
				to_visit_in_region.extend([n for n in graph[e] if n in to_visit])

		return counter



