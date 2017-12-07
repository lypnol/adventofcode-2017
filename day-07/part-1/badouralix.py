from runners.python import Submission
import re

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		nodes = set()
		children = set()
		pattern = re.compile('[a-z]+')
		for line in s.split('\n'):
			subnodes = re.findall(pattern, line)
			nodes = nodes.union([subnodes[0]])
			children = children.union(subnodes[1:])
		return nodes.difference(children).pop()
