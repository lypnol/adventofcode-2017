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
				a, b = ((a*16807) % 2147483647, (b*48271) % 2147483647)
				# print(a,b,n)
				n -= 1

				yield (a,b)



		return sum((1 if a%65536==b%65536 else 0) for a,b in generate(start_a, start_b, 40000000))



