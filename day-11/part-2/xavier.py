from runners.python import Submission


class XavierSubmission(Submission):
	def run(self, input):
		input = input.split(",")
		x, y, z = 0, 0, 0
		distances = []
		for mv in input:
			if mv == "n":
				y += 1
				z -= 1
			elif mv == "s":
				y -= 1
				z += 1
			elif mv == "sw":
				x += 1
				z += 1
			elif mv == "ne":
				x -= 1
				z -= 1
			elif mv == "nw":
				x += 1
				y += 1
			else:
				x -= 1
				y -= 1
			distances.append((abs(x) + abs(y) + abs(z)) // 2)
		return max(distances)
