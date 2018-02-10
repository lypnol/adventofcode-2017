from runners.python import Submission

class SouhaibSubmission(Submission):

  def run(self, s):
    # :param s: input in string format
    # :return: solution flag
    s = s.rstrip().split("\n")
    s = [list(map(int, x.split())) for x in s]
    return sum([max(x) - min(x) for x in s])
