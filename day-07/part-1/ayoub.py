from runners.python import Submission


class AyoubSubmission(Submission):

	def find_root(self, graph):
		for node in graph:
			has_parent = False
			for x in graph:
				if node in graph[x]:
					has_parent = True
					break
			if not has_parent:
				return node

	def run(self, s):
		graph = {}
		for line in s.split('\n'):
			parts = line.split()
			if len(parts) == 2:
				graph[parts[0]] = set()
			else:
				graph[parts[0]] = set(''.join(parts[3:]).split(','))
		return self.find_root(graph)
