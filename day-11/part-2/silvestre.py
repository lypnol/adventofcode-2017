from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        """
        clairement inspiré de xavier, j'ai pris un autre référentiel et une autre formule pour la forme
        """
        instructions = s.split(",")
        max_distance = 0
        s_axis = 0
        se_axis = 0
        for instruction in instructions:
            if instruction == "s":
                s_axis += 1
            if instruction == "n":
                s_axis -= 1
            if instruction == "se":
                se_axis += 1
            if instruction == "nw":
                se_axis -= 1
            if instruction == "ne":
                s_axis -= 1
                se_axis += 1
            if instruction == "sw":
                s_axis += 1
                se_axis -= 1
            max_distance = max(max_distance, max(abs(s_axis), abs(se_axis), abs(-s_axis-se_axis)))

        return max_distance
