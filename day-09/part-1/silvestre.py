from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        group_score = 1
        total_score = 0
        cl = list(s)
        for i, c in enumerate(cl):
            if c == '!':
                del cl[i+1]
        while '!' in cl:
            cl.remove('!')
        for i, c in enumerate(cl):
            if c == '{':
                total_score += group_score
                group_score += 1
            if c == '}':
                group_score -= 1
            if c == '<':
                del cl[i+1:(i+cl[i:].index('>'))]
            
        return total_score
