from runners.python import Submission

from collections import defaultdict

class DavidSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		pipes = s.split('\n')

		#
		# 1/ build the graph
		#
		adj_list = defaultdict(set)

		for pipe in pipes:
			[program_left, programs_right] = pipe.split(' <-> ')
			program_left = int(program_left)

			for program_right in [int(x) for x in programs_right.split(', ')]:
				adj_list[program_left].add(program_right)
				adj_list[program_right].add(program_left)


		#
		# 2/ count graphs
		#
		counter = 0

		visited = [False]*len(pipes)

		while not all(visited):
			counter += 1

			root = visited.index(False)
			# find nodes connected to the root using DFS
			to_visit = [root]

			while len(to_visit) > 0:
				e = to_visit.pop()
				visited[e] = True
				to_visit.extend([x for x in adj_list[e] if not visited[x]])

		return counter


