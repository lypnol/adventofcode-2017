from runners.python import Submission
import operator
from functools import reduce
from collections import defaultdict

class DavidSubmission(Submission):

	def __init__(self):
		super().__init__()
		self.pos = None
		self.skip_size = None
		self.lst = None
		self.n = None

	def compute_hash(self, value):
		self.n = 256
		self.lst = list(range(self.n))
		input = [ord(x) for x in value]
		lengths = input + [17, 31, 73, 47, 23]

		self.pos = 0 # current position index
		self.skip_size = 0

		# 64 rounds
		for _ in range(64):
			self.run_round(lengths)

		dense_hash = [self.hexa(x) for x in self.compute_dense_hash()]

		return "".join(dense_hash)

	def hexa_to_bin(self, value):
		return "{0:04b}".format(int(value, 16))


	def compute_dense_hash(self):
		# xor elements in a list
		def xor(l):
			return reduce(operator.xor, l, 0)

		return [xor(self.lst[16*k:16*(k+1)]) for k in range(16)]

	def hexa(self, value):
		return format(value, '02x')

	def run_round(self, lengths):
		n = self.n

		for length in lengths:
			i = self.pos
			j = (self.pos+length-1)

			for k in range(length//2):
				tmp = self.lst[(j-k)%n]
				self.lst[(j-k)%n] = self.lst[(i+k)%n]
				self.lst[(i+k)%n] = tmp

			self.pos = (self.pos + length + self.skip_size) % n
			self.skip_size += 1

	def neighbors(self, pos):
		def is_correct(pos):
			x, y = pos
			return x >= 0 and y >= 0 and x < 128 and y < 128

		x,y = pos
		return [p for p in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)] if is_correct(p)]



	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here

		graph = defaultdict(set)
		hashes = [self.compute_hash("{}-{}".format(s, str(i))) for i in range(128)]

		count_ones = 0
		for i, full_hash in enumerate(hashes):
			for j, h in enumerate(full_hash):
				for k, b in enumerate(self.hexa_to_bin(h)):
					node = (i,4*j+k)
					if b == "1":
						count_ones += 1
						if node not in graph:
							graph[node] = set()

						for neighbor in self.neighbors(node):
							if not neighbor in graph or not graph[neighbor] == False:
								graph[neighbor].add(node)
					else:
						graph[node] = False


		counter = 0
		visited = [False] * count_ones
		ones = [k for k in graph.keys() if not graph[k] == False]
		reversed_ones = {v:k for k,v in enumerate(ones)}

		while not all(visited):
			counter += 1
			root = ones[visited.index(False)]
			to_visit = [root]

			while len(to_visit) > 0:
				e = to_visit.pop()
				visited[reversed_ones[e]] = True
				to_visit.extend([n for n in graph[e] if not visited[reversed_ones[n]]])

		return counter



