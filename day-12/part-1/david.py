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
		# 2/ count nodes related to 0 with a DFS algorithm
		#

		visited = [False]*len(pipes)
		connected = [False]*len(pipes)
		to_visit = [0]

		while len(to_visit) > 0:
			node = to_visit.pop()
			visited[node] = True

			to_visit.extend([x for x in adj_list[node] if not visited[x]])

			for child in adj_list[node]:
				connected[child] = True

		return connected.count(True)
