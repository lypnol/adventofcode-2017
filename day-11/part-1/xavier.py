from runners.python import Submission
from collections import Counter


class XavierSubmission(Submission):
	"""Thanks to https://www.redblobgames.com/grids/hexagons"""
	def run(self, input):
		count = Counter(input.split(","))
		v_axis = count["n"] - count["s"]
		d1_axis = count["sw"] - count["ne"]
		d2_axis = count["nw"] - count["se"]
		return (abs(d1_axis - d2_axis) + abs(d2_axis + v_axis) + abs(v_axis + d1_axis)) / 2
