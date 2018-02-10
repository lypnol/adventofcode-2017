from runners.python import Submission

class SouhaibSubmission(Submission):

	def run(self, s):
		# :param s: input in string format
		# :return: solution flag

    s = [sorted(list(map(int, x.split())), reverse = True) for x in s.rstrip().split("\n")]
    s = [line[i] // line[j] for line in s for i in range(len(line)) for j in range(i+1, len(line)) if line[i] % line[j] == 0]
    return sum(s)
