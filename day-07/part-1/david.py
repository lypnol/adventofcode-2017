from runners.python import Submission

import re

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# your solution code goes here
		lines = s.split("\n")

		names = set()
		all_children = set()
		for line in lines:
			name, weight, children = self.handle_line(line)
			names.add(name)
			all_children = all_children.union(children)

		bottom_program = names - all_children
		assert(len(bottom_program) == 1)

		return list(bottom_program)[0]



	def handle_line(self, line):
		match = re.search('^(?P<name>[a-z]+)\s\((?P<weight>[0-9]+)\)(?P<end>.*)$', line)

		end = match.group('end')
		children = []
		if end.startswith(' ->'):
			children = end[4:].split(', ')

		return (match.group('name'), match.group('weight'), children)




