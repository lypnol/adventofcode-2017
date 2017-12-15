from runners.python import Submission

class DavidSubmission(Submission):



	def run(self, s):
		# :param s: input in string format
		# :return: solution flag
		# Your code goes here
		[start_a, start_b] = [int(x[24:]) for x in s.split('\n')]

		def generate(start_a, start_b, n):
			a, b = (start_a, start_b)
			while n > 0:
				while True:
					a = (a*16807) % 2147483647
					if a%4 == 0: break

				while True:
					b = (b*48271) % 2147483647
					if b%8 == 0: break

				n -= 1

				yield (a,b)



		return sum((1 if (a & 0xffff)==(b & 0xffff) else 0) for a,b in generate(start_a, start_b, 5000000))



