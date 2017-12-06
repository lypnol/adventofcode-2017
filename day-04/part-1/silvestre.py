from submission import Submission

class SilvestreSubmission(Submission):

    def run(self,s):
        sentences = s.split("\n")
        count = 0
        for sentence in sentences:
            valid = True
            words =  sentence.split(" ")
            for word in words:
                if words.count(word) > 1:
                    valid = False
            if valid == True:
                count += 1
        return count