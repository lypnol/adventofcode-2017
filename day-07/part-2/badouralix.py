from runners.python import Submission
from collections import Counter
import re
import pprint

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		tree = dict()
		pattern = re.compile('\w+')

		for line in s.split('\n'):
			node, weight, *children = re.findall(pattern, line)
			tree[node] = {
				"node_weight": int(weight),
				"children": children,
				"parent": tree.get(node, {}).get("parent", '')
			}
			for child in children:
				tree[child] = tree.get(child, {})
				tree[child].update({"parent": node})

		root_tree = self.root(tree)
		self.subtree_weight(root_tree, tree)
		return self.correct_weight(root_tree, tree)

	def root(self, tree):
		return list(filter(lambda node: tree[node]["parent"] == '', tree)).pop()

	def subtree_weight(self, node, tree):
		weight = tree[node]["node_weight"]
		children_weights = Counter()
		for child in tree[node]["children"]:
			try:
				subtree_weight += tree[child]["subtree_weight"]
			except:
				child_weight = self.subtree_weight(child, tree)
				children_weights[child_weight] += 1
				weight += child_weight
		tree[node].update({"children_error": len(children_weights) > 1})
		tree[node].update({"children_weights": children_weights})
		tree[node]["subtree_weight"] = weight
		return weight

	def correct_weight(self, node, tree, balanced_weight=None):
		if not tree[node]["children_error"]:
			return balanced_weight - tree[node]["children_weights"].most_common()[0][0] * len(tree[node]["children"])
		else:
			balanced_weight = tree[node]["children_weights"].most_common()[0][0]
			for child in tree[node]["children"]:
				if tree[child]["children_error"]:
					return self.correct_weight(child, tree)
				if tree[child]["subtree_weight"] != balanced_weight:
					child_error = child
					break

			return self.correct_weight(child_error, tree, balanced_weight)
