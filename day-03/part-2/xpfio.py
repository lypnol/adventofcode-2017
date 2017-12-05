from submission import Submission


class XpfioSubmission(Submission):

	def run(self, s):
		n = int(s)
		spiral = {}
		value = 1
		x = 0
		y = 0

		#Init
		spiral[(x,y)] = value
		x += 1

		while value <= n:
			value = 0
			# Check neighbors
			to_check = [
				(x+1,y+1),
				(x+1,y),
				(x+1,y-1),
				(x,y+1),
				# (x,y),
				(x,y-1),
				(x-1,y+1),
				(x-1,y),
				(x-1,y-1),
			]
			for a in to_check:
				if a in spiral:
					value += spiral[a]
			spiral[(x,y)] = value

			# Move
			to_check = [
				(x-1,y),
				(x,y+1),
				(x+1,y),
				(x,y-1)
			]
			direction = ''
			for a in to_check:
				if a in spiral:
					direction += '1'
				else:
					direction += '0'
			
			if direction == '1000':
				y = y+1
			elif direction == '0001':
				x = x -1
			elif direction == '0011':
				x = x-1
			elif direction == '0010':
				y = y-1
			elif direction == '0110':
				y = y-1
			elif direction == '0100':
				x = x+1
			elif direction == '1100':
				x = x+1
			elif direction == '1001':
				y = y+1

		return value

