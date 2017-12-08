from runners.python import Submission


class LoicSubmission(Submission):
	head = {str: []}
	weight = {}
	correction_price = 0

	def run(self, s):
		head = []
		queue = []
		self.head = {}
		self.weight = {}
		self.correction_price = 0
		for line in s.split("\n"):
			split = line.split()
			if "->" in line:
				self.head[split[0].strip()] = line.split("->")[1].split(", ")
				head.append(line.split()[0])
				for subline in line.split("->")[1].split(", "):
					queue.append(subline.strip())
			self.weight[split[0].strip()] = int(split[1].replace('(', '').replace(')', '').strip())

		for line in queue:
			if line in head:
				head.remove(line)

		self.get_price(head[0])

		return self.correction_price

	def get_price(self, node):
		if node not in self.head.keys():
			return self.weight[node]
		prices = {n.strip(): self.get_price(n.strip()) for n in self.head[node]}
		if self.correction_price == 0 and len(set(prices.values())) > 1:
			compte = {}.fromkeys(set(prices.values()), 0)
			devious_price = 0
			correct_price = 0
			devious_node = ""
			for val in prices.values():
				compte[val] += 1
			for p in compte:
				if compte[p] == 1:
					devious_price = int(p)
				else:
					correct_price = int(p)
			for n, pr in prices.items():
				if pr == devious_price:
					devious_node = n
			self.correction_price = self.weight[devious_node] - devious_price + correct_price
		return sum(prices.values()) + self.weight[node]

