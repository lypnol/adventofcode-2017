from submission import Submission

class SilvestreSubmission(Submission):
    """
    On essaye de stocker seulement la position de 0 et de celui qui suit
    """
    
    def run(self, s):
        s = int(s)
        d = {}
        
        # Initialisation du buffer
        pos_0 = 0
        next_to_0 = None
        lenght = 1   # Ceci est la "longueur" du buffer
        old_pos = 0

        # On se lance dans le tourbilol
        LOL = 50*1000*1000
        while lenght < LOL:
            new_pos = (old_pos + s) % lenght

            if new_pos < pos_0:
                pos_0 += 1
            elif new_pos == pos_0:
                next_to_0 = lenght
            
            old_pos = new_pos +1
            lenght += 1
        
        #import pdb; pdb.set_trace()
        return next_to_0