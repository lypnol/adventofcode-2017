from runners.python import Submission

class LoicSubmission(Submission):

	def run(self, s):
		data = s.split("\n")
		head = []
		queue = []

		for line in data:
			if "->" in line:
				head.append(line.split()[0])
				for subline in line.split("->")[1].split(", "):
					queue.append(subline.strip())

		for line in queue:
			if line in head:
				head.remove(line)

		return head[0]
