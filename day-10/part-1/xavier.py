from runners.python import Submission


class XavierSubmission(Submission):
	def run(self, s):
		s = list(map(int, s.split(",")))
		c_list = list(range(256))
		cur_pos = 0
		skip = 0
		for length in s:
			buffer = [c_list[(cur_pos + i) % 256] for i in range(length)]
			buffer = buffer[::-1]
			for i in range(length):
				c_list[(cur_pos + i) % 256] = buffer[i]
			cur_pos += length + skip
			cur_pos = cur_pos % 256
			skip += 1
		return c_list[0] * c_list[1]
