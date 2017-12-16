from runners.python import Submission


class MathieuSubmission(Submission):
    """j'ai refait la comparaison entre a et b, en m'inspirant des algos de Jules et David
    Mon algo était vraiment trop long sinon..."""
    def run(self, s):
        val_a = int(s.split("\n")[0].replace("Generator A starts with ", ""))
        val_b = int(s.split("\n")[1].replace("Generator B starts with ", ""))
        count = 0
        pairs=0
        while pairs<40000000:
            val_a = (val_a * 16807)%2147483647
            val_b = (val_b * 48271)%2147483647
            if (val_a-val_b)&0xffff==0:
                count += 1
            pairs+=1
        return count
