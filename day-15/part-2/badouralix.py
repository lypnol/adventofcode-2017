from runners.python import Submission

class BadouralixSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		self.start_a = int(s.split('\n')[0].split()[4])
		self.start_b = int(s.split('\n')[1].split()[4])
		generator = self.generator()
		result = 0

		for _ in range(5000000):
			a, b = next(generator)
			result += (a ^ b) & 0xffff == 0

		return result

	def generator(self):
		a, b = self.start_a, self.start_b
		while True:
			while True:
				a = (a * 16807) % 0x7fffffff
				if not (a & 0b11):
					break
			while True:
				b = (b * 48271) % 0x7fffffff
				if not (b & 0b111):
					break
			yield a, b
