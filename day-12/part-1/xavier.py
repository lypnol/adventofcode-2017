from runners.python import Submission


class XavierSubmission(Submission):
	def run(self, s):
		s = [k.split(" <-> ") for k in s.split("\n")]

		queue = [s[0]]
		visited = set()

		while queue:
			for node in queue[0][1].split(", "):
				if node not in visited:
					queue.append(s[int(node)])
					visited.add(node)
			queue.pop(0)
		return len(visited)
