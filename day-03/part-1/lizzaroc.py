from submission import Submission
from math import *

class LizzarocSubmission(Submission):

	def run(self, s):
		k = int(s)
		h = floor((sqrt(k) - 1)/2)
		rl_corner = (2*h+1)**2
		dmin = min([abs(rl_corner + (2*i+1)*(h+1) - k) for i in range(4)])
		return h + 1  + dmin

