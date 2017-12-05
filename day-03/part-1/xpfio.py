from runners.python import Submission
import math

class XpfioSubmission(Submission):

	def run(self, s):
		n = int(s)-1
		m = math.ceil(math.sqrt(n))
		k = (m-1)/2 if m%2 == 1 else (m/2 if n>=m*(m+1) else m/2 - 1)

		if n <= (2*k+1)**2:
			return int(abs(n-4*k**2-3*k)+abs(k))
		elif n <= 2*(k+1)*(2*k+1):
			return int(abs(k+1)+abs(4*k**2+5*k+1-n))
		elif n<= 4*(k+1)**2:
			return int(abs(4*k**2+7*k+3-n)+abs(-k-1))
		else:
			return int(abs(-k-1)+abs(n-4*k**2-9*k-5))
