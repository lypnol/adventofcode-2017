from functools import reduce
from submission import Submission

class SilvestreSubmission(Submission):
    
    def run(self, s):
        instructions = []
        for raw in s.split(","):
            args = raw[1:].split("/")
            if len(args) == 1:
                args.append("")
            instructions.append({
                "moves": raw[0],
                "arg1": args[0],
                "arg2": args[1]})

        """
        one instruction is a dict : 
        {
            "moves" : {'x','s','p'},
            "arg1" : {[0-15],[a-p]},
            "arg2" (optional) : {[0-15],[a-p]}
        }
        """
        programs = ['a','b','c','d','e','f','g','h','i','j','k', 'l', 'm', 'n', 'o', 'p']
        
        for instruction in instructions:
            if instruction["moves"] == 's':
                i = int(instruction["arg1"])
                programs = programs[-i:] + programs[:16-i]
            
            elif instruction["moves"] == 'x':
                i = int(instruction["arg1"])
                j = int(instruction["arg2"])
                temp = programs[i]
                programs[i] = programs[j]
                programs[j] = temp
            
            elif instruction["moves"] == "p":
                a = instruction["arg1"]
                b = instruction["arg2"]
                i = programs.index(a)
                j = programs.index(b)
                programs[i] = b
                programs[j] = a

        return "".join(programs)