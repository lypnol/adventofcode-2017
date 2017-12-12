from runners.python import Submission


class XavierSubmission(Submission):
	def run(self, s):
		s = [k.split(" <-> ") for k in s.split("\n")]
		s = [[int(k[0])] + list(map(int, k[1].split(", "))) for k in s]
		n = len(s)
		queue = [s[0]]
		visited = set()
		visited.add(s[0][0])
		comp = 0

		while visited:
			while queue:
				for node in queue[0][1:]:
					if node not in visited:
						queue.append(s[node])
						#visited.add(node)
						visited.add(node)
				queue.pop(0)
			left_to_visit = set(range(n)) - visited
			comp += 1
			try:
				queue.append(s[left_to_visit.pop()])
			except:
				return comp