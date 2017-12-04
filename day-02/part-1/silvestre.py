from submission import Submission

class SilvestreSubmission(Submission):
    """
    J'ai copié le code de chloé car je ne m'en sortais pas (j'ai jamais fait de python avant)
    J'ai beaucoup BEAUCOUP appris au passage en comprenant, merci !!! 
    """

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        table_str = [row.split("\t") for row in s.split("\n")]
        table_int = [list(map(int,row)) for row in table_str]
        return sum(max(row) - min(row) for row in table_int)
