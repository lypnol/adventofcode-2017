from runners.python import Submission
from re import match

class XavierSubmission(Submission):

	def run(self, s):
		s = s.split("\n")

		# All nodes
		all_nodes = [k.split(" (")[0] for k in s]

		# Nodes with parent
		nodes_with_parent = [k.split("-> ")[1:] for k in s]
		nodes_with_parent = [k for k in nodes_with_parent if k != []]

		nodes_with_parent_set = []
		for k in nodes_with_parent:
			nodes_with_parent_set += k[0].split(", ")
		nodes_with_parent_set = set(nodes_with_parent_set)

		for k in all_nodes:
			if k not in nodes_with_parent_set:
				return k