from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        """
        clairement inspiré de xavier, j'ai pris un autre référentiel et une autre formule pour la forme
        """
        instructions = s.split(",")
        s_axis = instructions.count("s") - instructions.count("n") + instructions.count("sw") - instructions.count("ne") 
        se_axis = instructions.count("se") - instructions.count("nw") + instructions.count("ne") - instructions.count("sw")
        return max(abs(s_axis), abs(se_axis), abs(-s_axis-se_axis))
