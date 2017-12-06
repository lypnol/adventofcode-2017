from submission import Submission


class AyoubSubmission(Submission):

	def run(self, s):
		blocks = list(map(int, s.split()))
		n = len(blocks)
		cycles = 0
		seen = {}
		while tuple(blocks) not in seen:
			# Register as seen
			seen[tuple(blocks)] = cycles
			# Find first maximum
			i = 0
			for j in range(n):
				if blocks[j] > blocks[i]: 
					i = j
			# Get value of maximum and reset to 0
			v = blocks[i]
			blocks[i] = 0
			offset = (i+1)%n
			# Spread value over all blocks
			c = 0
			# Start by counting full loops (v // n)
			while c < n:
				blocks[(offset + c)%n] += v // n
				c += 1
			c = 0
			# Complete with what's left
			while c < v%n:
				blocks[(offset + c)%n] += 1
				c += 1
			cycles += 1
		return cycles - seen[tuple(blocks)]