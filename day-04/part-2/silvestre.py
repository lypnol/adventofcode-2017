from submission import Submission

class SilvestreSubmission(Submission):

    def run(self,s):
        sentences = s.split("\n")
        count = 0
        for sentence in sentences:
            valid = True
            words =  sentence.split(" ")
            dl = []
            for word in words:
                cl = list(word)
                d= {}
                for c in cl:
                    d[c] = 1 if c not in d.keys() else d[c]+1
                dl.append(d)
            for d in dl:
                if dl.count(d)>1:
                    valid=False
            if valid == True:
                count += 1
        return count