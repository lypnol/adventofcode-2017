from runners.python import Submission
import operator
from functools import reduce

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

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here

		hashes = (self.compute_hash("{}-{}".format(s, str(i))) for i in range(128))

		counter = 0
		for full_hash in hashes:
			counter += sum(self.hexa_to_bin(h).count("1") for h in full_hash)

		return counter

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
