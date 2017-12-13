from runners.python import Submission
import re

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		tree = self.parse(s)
		remaining = set(range(len(tree)))
		result = 0
		while remaining:
			result += 1
			root = remaining.pop()
			q = set(tree[root])
			while q:
				node = q.pop()
				remaining.discard(node)
				q = q.union(tree[node])
				q.intersection_update(remaining)
		return result

	def parse(self, s):
		tree = []
		index = 0
		for line in s.split('\n'):
			tree.append([])
			for neighbor in re.split(' |, ', line)[2:]:
				tree[index].append(int(neighbor))
			index += 1
		return tree
