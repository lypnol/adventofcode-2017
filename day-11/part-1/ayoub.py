from runners.python import Submission
import fibonacci_heap_mod as hq


class AyoubSubmission(Submission):

	direction = {
		'ne': (1, 0),
		'n': (1, -1),
		'nw': (0, -1),
		'sw': (-1, 0),
		's': (-1, 1),
		'se': (0, 1)
	}

	@staticmethod
	def manhattan(a, b): 
		return abs(a[0]-b[0])+abs(a[1]-b[1])

	def a_star(self, start, end, heur):
		dist = {start: 0}
		visited = set()
		Q = hq.Fibonacci_heap()
		Q_index = {}
		Q_index[start] = Q.enqueue(start, 0)
		while Q:
			current = Q.dequeue_min().get_value()
			visited.add(current)

			if heur(current, end) < 0.1:
				return dist[current]

			for child in self.get_children(current):
				if child in visited: 
					continue
				if child not in dist:
					dist[child] = dist[current] + 1
					Q_index[child] = Q.enqueue(child, dist[child] + heur(child, end))
				elif child in dist and dist[child] > dist[current] + 1:
					dist[child] = dist[current] + 1
					Q.decrease_key(Q_index[child], dist[child] + heur(child, end))

	def get_children(self, node):
		x, y = node
		children = []
		for u, v in self.direction.values():
			children.append((x+u, y+v))
		return children

	def run(self, s):
		start = (0, 0)
		end = (0, 0)
		for move in s.split(','):
			u, v = self.direction[move]
			end = (end[0]+u, end[1]+v)
		
		return self.a_star(start, end, self.manhattan)