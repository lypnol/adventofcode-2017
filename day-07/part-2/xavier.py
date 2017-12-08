from runners.python import Submission
from re import search


class XavierSubmission(Submission):
	dict = {}

	def get_root(self):
		nodes_with_parent_set = set()
		for k, v in self.dict.items():
			for i in v['children']:
				nodes_with_parent_set.add(i)
		for k, v in self.dict.items():
			if k not in nodes_with_parent_set:
				return v

	def process_line(self, line):
		processed_input = search("^(?P<root>[a-z]+)\s\((?P<weight>[0-9]+)\)( -> )?(?P<children>[a-z,\s]+)*$", line)
		children = []
		try:
			children = processed_input.group('children').split(', ')
		except:
			pass
		finally:
			return {"root": processed_input.group("root"), "weight": int(processed_input.group("weight")),
			        "children": children, "total_weight": int(processed_input.group("weight")), "parent": ""}

	def update_weights(self, root_node):
		children = [v for k, v in self.dict.items() if v["root"] in root_node["children"]]
		for child in children:
			child["parent"] = root_node["root"]
			self.update_weights(child)
			children_weights = [v["total_weight"] for k, v in self.dict.items() if v["root"] in child["children"]]
			child["total_weight"] += sum(children_weights)

	def get_error(self, root_node, return_value=False):
		children = [v for k, v in self.dict.items() if k in root_node["children"]]
		children_weights = [v["total_weight"] for v in children]
		if len(set(children_weights)) == 1:
			return self.get_error(self.dict[root_node["parent"]], return_value=True)
		else:
			min_weight, max_weight = min(children_weights), max(children_weights)
			min_count, max_count = children_weights.count(min_weight), children_weights.count(max_weight)
			if not return_value:
				if min_count == 1:
					return self.get_error(children[children_weights.index(min_weight)])
				elif max_count == 1:
					return self.get_error(children[children_weights.index(max_weight)])
			else:
				if min_count == 1:
					return children[children_weights.index(min_weight)] + max_weight - min_weight
				elif max_count == 1:
					return children[children_weights.index(max_weight)]["weight"] - max_weight + min_weight

	def run(self, s):
		self.dict = {}
		s = s.split("\n")
		for k in s:
			p = self.process_line(k)
			self.dict[p['root']] = p
		root = self.get_root()
		self.update_weights(root)
		return self.get_error(root)
