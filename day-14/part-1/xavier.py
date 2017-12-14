from functools import reduce

from runners.python import Submission

class XavierSubmission(Submission):

	"""Hash calculation from silvestre"""
	def hash(self, s):
		lengths = list(map(ord, s)) + [17, 31, 73, 47, 23]
		main_list = list(range(256))

		current_position = 0
		skip_size = 0
		for i in range(64):
			for length in lengths:
				i1 = current_position
				i2 = (current_position + length) % 256

				if i1 < i2:
					sublist = main_list[i1: i2]
					sublist.reverse()

					l1 = main_list[:i1]
					l2 = main_list[i2:]

					main_list = l1 + sublist + l2
				elif i1 > i2:
					sublist = main_list[i1:] + main_list[:i2]
					assert (len(sublist) == length)
					sublist.reverse()

					if i2 != 0:
						main_list = sublist[-i2:] + main_list[i2:i1] + sublist[:(256 - i1)]
					else:
						main_list = main_list[i2:i1] + sublist[:(256 - i1)]

				current_position = (current_position + length + skip_size) % 256
				skip_size += 1

				assert (len(main_list) == 256)

		sparse_hash = [main_list[i:i + 16] for i in range(0, len(main_list), 16)]

		dense_hash = [reduce(lambda i, j: int(i) ^ int(j), block) for block in sparse_hash]

		final_output = "".join(list(map('{0:02x}'.format, dense_hash)))

		return final_output

	def run(self, s):
		count = 0
		for k in range(128):
			count += list(bin(int(self.hash(s+"-"+str(k)), 16))[2:].zfill(128)).count("1")
		return count

