from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        """
        Ceci est une tentative d'optimisation de l'algo de Mathieu.                
        """
        layers = [(int(x.split(': ')[0]), int(x.split(': ')[1])) for x in s.split('\n')]

        #Number of smallest elements targeted
        x = 3

        smallest_l = []
        layers_c = layers.copy()
        smallest_l = sorted(layers_c, key= lambda x: x[1])[:x]

        caught = True
        delay = 0
        while caught:
            
            for layer, r in smallest_l:
                if (delay - layer) % ((r -1) * 2) == 0:
                    delay += 1
                    break
            
            caught = False
            for layer, depth in layers:
                if (delay + layer) % (2 * depth - 2) == 0:
                    caught = True
                    delay += 1
                    break
        return delay
