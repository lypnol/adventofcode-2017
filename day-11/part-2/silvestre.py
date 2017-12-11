from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        """
        clairement inspiré de xavier, j'ai pris un autre référentiel et une autre formule pour la forme
        """
        instructions = s.split(",")
        max_distance = 0
        n_axis = 0
        ne_axis = 0
        for instruction in instructions:
            if instruction == "n":
                n_axis += 1
            if instruction == "s":
                n_axis -= 1
            if instruction == "ne":
                ne_axis += 1
            if instruction == "sw":
                ne_axis -= 1
            max_distance = max(max_distance, max(abs(n_axis), abs(ne_axis), abs(-n_axis-ne_axis)))

        return max_distance
