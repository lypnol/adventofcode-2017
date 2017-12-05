from submission import Submission


class AyoubSubmission(Submission):

	def find_matrix_layer(self, x):
		# Finds which layer a given int is on in the matrix
		# Returns the layer number and the value of the first
		# element from which we start building the spiral
		# For example 12 is on layer 3 which started from 10

		k = 1
		v1 = 1
		v = v1 + 8 * (k - 1)
		while v < x:
			v1 = v
			v = v1 + 8 * (k - 1)
			k += 1
		return (k-1, v1+1)

	def find_index_on_layer(self, k, v, x):
		# Given a sipral layer and its first value
		# Returns the index of x its side of the layer 
		# relative to middle
		# dimension of matrix n x n
		n = 2 * (k - 1) + 1

		side = (x - v) // (n-1)
		index = x - (v + (n-1) * side) - (n // 2 - 1)

		return index

	def run(self, s):
		x = int(s)
		k, v = self.find_matrix_layer(x)
		i = self.find_index_on_layer(k, v, x)
		return abs(i) + abs(k-1)
