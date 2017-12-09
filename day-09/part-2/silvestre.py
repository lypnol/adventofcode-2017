from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        count = 0
        
        cl = list(s)
        for i, c in enumerate(cl):
            if c == '!':
                del cl[i+1]
        while '!' in cl:
            cl.remove('!')
        for i, c in enumerate(cl):
            if c == '<':
                count += len(cl[i+1:(i+cl[i:].index('>'))])
                del cl[i+1:(i+cl[i:].index('>'))]
            
        return count
