from runners.python import Submission


class XavierSubmission(Submission):

	def run(self, s):
		s = list(map(ord, s)) + [17, 31, 73, 47, 23]
		c_list = list(range(256))
		cur_pos = 0
		skip = 0
		for length in s*64:
			buffer = [c_list[(cur_pos+i)%256] for i in range(length)]
			buffer = buffer[::-1]
			for i in range(length):
				c_list[(cur_pos+i)%256] = buffer[i]
			cur_pos = (cur_pos + length + skip) % 256
			skip += 1
		hashes = [c_list[16*i] for i in range(16)]
		for i in range(16):
			for j in range(1,16):
				hashes[i] ^= c_list[i*16+j]
		return ''.join(map(lambda x: hex(x)[2:].zfill(2), hashes))
