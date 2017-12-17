from collections import defaultdict
from submission import Submission

class SilvestreSubmission(Submission):
    """
    Ceci n'est pas de la doc
    """
    
    def run(self, s):
        s = int(s)
        buff = defaultdict(int)
        buff[0] = 0
        while len(buff) < 2018:
            old_pos = buff[len(buff)-1]
            new_pos = (old_pos + s) % len(buff)
            for k, value in buff.items():
                if value >= new_pos +1 :
                    buff[k] += 1
            buff[len(buff)] = new_pos + 1

        #import pdb; pdb.set_trace()
        pos_2017 = buff[2017]
        result = "You failed"
        for key in buff:
            #import pdb; pdb.set_trace()
            if buff[key] == (pos_2017+1):
                result = key  
        return result