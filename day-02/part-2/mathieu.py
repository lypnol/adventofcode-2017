from submission import Submission


class MathieuSubmission(Submission):

	def run(self, s):
		inputs=[list(map(int,line.split())) for line in s.split('\n')]
		res=0
		for line in inputs:
			for num1 in line:
				for num2 in line:
					if num1!=num2 and num1%num2==0:
						res+=num1/num2
		return int(res)

