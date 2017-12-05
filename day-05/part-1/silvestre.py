from submission import Submission

class SilvestreSubmission(Submission):

    def run(self,s):
        instructions = list(map(int, s.split("\n")))
        count = 0
        i = 0
        try:
            while True:
                if i<0:
                    raise IndexError
                instruction = instructions[i]
                instructions[i] += 1
                i = i+instruction
                count +=1
        except IndexError:
            pass
        return count