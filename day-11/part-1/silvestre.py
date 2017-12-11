from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        """
        clairement inspiré de xavier, j'ai pris un autre référentiel et une autre formule pour la forme
        """
        instructions = s.split(",")
        n_axis = instructions.count("n") - instructions.count("s")
        ne_axis = instructions.count("ne") - instructions.count("sw")

        return max(abs(n_axis), abs(ne_axis), abs(-n_axis-ne_axis))
