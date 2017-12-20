from runners.python import Submission
import re

class MathieuSubmission(Submission):

    def re_acceleration(self,line):
        groups=re.search(r'a=<(-?\d+),(-?\d+),(-?\d+)>',line)
        return [int(acc) for acc in groups.group(1,2,3)]

    def run(self, s):
        accelerations=[self.re_acceleration(line) for line in s.split('\n')]
        return accelerations.index(min(accelerations,key=lambda x:abs(x[0])+abs(x[1])+abs(x[2])))
