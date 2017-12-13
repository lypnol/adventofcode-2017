from runners.python import Submission
from collections import deque
import re

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		tree = self.parse(s)
		visited = [True] + [False] * (len(tree) - 1)
		results = 1
		d = deque(tree[0])
		while d:
			node = d.pop()
			if not visited[node]:
				visited[node] = True
				results += 1
				d.extend(tree[node])
		return results

	def parse(self, s):
		tree = []
		index = 0
		for line in s.split('\n'):
			tree.append([])
			for neighbor in re.split(' |, ', line)[2:]:
				tree[index].append(int(neighbor))
			index += 1
		return tree
