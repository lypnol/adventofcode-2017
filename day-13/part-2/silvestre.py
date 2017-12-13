from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        layers = {}
        for line in s.split("\n"):
            parts = line.split(": ")
            layers[int(parts[0])] = int(parts[1])
            max_depth = int(parts[0])
        
        """
        a layer of layers is :
            0 (depth) : 3 (range)                
        """
        caught = True
        waiting_time = 0
        while caught:
            caught = False
            for layer in layers.items():
                c_time = layer[0] + waiting_time
                if c_time % (2*(layer[1]-1)) == 0:
                        caught = True
                        waiting_time += 1
                        break
        return waiting_time
