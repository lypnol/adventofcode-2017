from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        layers = {}
        for line in s.split("\n"):
            parts = line.split(": ")
            layers[int(parts[0])] = {
                "range" : int(parts[1]),
                "s_pos" : 1,
                "des" : True
            }
            max_depth = int(parts[0])
        
        """
        a layer of layers is :
            0 (depth) : {
                "range" : 3,
                "s_pos": 1,
                "des": False
            }
        """
        severity = 0
        for cursor_pos in range(max_depth+1):
            if cursor_pos in layers:
                c_layer = layers[cursor_pos]
                if c_layer["s_pos"] == 1:
                    severity += cursor_pos*c_layer["range"]
            for layer in layers.values():
                #import pdb; pdb.set_trace()
                pos = layer["s_pos"]
                rg = layer["range"]
                des = layer["des"]
                layer["s_pos"] = pos + 1 if des else pos -1
                layer["des"] = not des if layer["s_pos"] == 1 or layer["s_pos"] == rg else des
        return severity
            