from runners.python import Submission

import re
from queue import PriorityQueue
from collections import Counter, defaultdict

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		lines = s.split("\n")

		children = dict()
		weights = dict()
		costs = dict()
		all_children = set()
		heights = defaultdict(list) # stores n :-> list of elements having h(n) in the tree

		for i, line in enumerate(lines):
			name, weight, leaves = self.handle_line(line)

			children[name] = leaves
			weights[name] = weight

			all_children = all_children.union(leaves)

		# find bottom program
		bottom_programs = set(children.keys()) - all_children
		assert(len(bottom_programs) == 1)
		bottom_program = list(bottom_programs)[0]

		# compute the heights
		q = PriorityQueue()
		q.put((0, bottom_program))

		while not q.empty():
			h, e = q.get()
			heights[h].append(e)
			for c in children[e]:
				q.put((h+1, c))

		max_height = max(heights.keys())
		height = max_height

		while True:
			for node in heights[height]:
				# are all the costs of the children the same ?
				if len(children[node]) > 0:
					# node is not a leaf

					# find most common cost of the children
					most_common_cost, count = Counter([costs[x] for x in children[node]]).most_common(1)[0]
					if count < len(children[node]):
						# not all the children have the same cost
						for c in children[node]:
							if costs[c] != most_common_cost:
								return weights[c] + most_common_cost - costs[c]


					costs[node] = sum((costs[x] for x in children[node])) + weights[node]
				else:
					costs[node] = weights[node]

			height -= 1



	def handle_line(self, line):
		match = re.search('^(?P<name>[a-z]+)\s\((?P<weight>[0-9]+)\)(?P<end>.*)$', line)

		end = match.group('end')
		children = []
		if end.startswith(' ->'):
			children = end[4:].split(', ')

		return (match.group('name'), int(match.group('weight')), children)




