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

	def get_total_weight(self, graph, weight, root):
		if root in self._cache:
			return self._cache[root]
		s = weight[root]
		for child in graph[root]:
			s += self.get_total_weight(graph, weight, child)
		self._cache[root] = s
		return self._cache[root]

	def is_balanced(self, graph, weight, root):
		if len(graph[root]) == 0:
			return True
		return len(set([ self.get_total_weight(graph, weight, child) for child in graph[root] ])) == 1

	def find_right_weight(self, graph, weight, root):
		if len(graph[root]) == 0 or self.is_balanced(graph, weight, root):
			return None
		# Calculate total weights of children trees
		children_weights = {
			child: self.get_total_weight(graph, weight, child) for child in graph[root]
		}
		# Look for the wrong weight
		wrong_child = None
		wanted_weight = 0
		occ = {}
		for w in children_weights.values():
			if w in occ: 
				occ[w] += 1
				wanted_weight = w
			else: occ[w] = 1
		for child, w in children_weights.items():
			if occ[w] == 1:
				wrong_child = child
				break
		# If the wrong child subtree is not balanced then keep on searching 
		if not self.is_balanced(graph, weight, wrong_child):
			return self.find_right_weight(graph, weight, wrong_child)

		# If there is a wrong weight found the return the corrected one
		diff = abs(children_weights[wrong_child] - wanted_weight)
		if weight[wrong_child] > diff:
			return weight[wrong_child] - diff
		return weight[wrong_child] + diff

	def run(self, s):
		graph = {}
		weight = {}
		for line in s.split('\n'):
			parts = line.split()
			weight[parts[0]] = int(parts[1][1:-1])
			if len(parts) == 2:
				graph[parts[0]] = set()
			else:
				graph[parts[0]] = set(''.join(parts[3:]).split(','))
		
		root = self.find_root(graph)
		self._cache = {}
		return self.find_right_weight(graph, weight, root)