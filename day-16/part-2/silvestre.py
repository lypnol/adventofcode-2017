from submission import Submission

class SilvestreSubmission(Submission):
    """
    J'ai tenté un truc à base de maketrans + translate mais ça marche juste pas .... du coup j'ai copié Div.
    """
    
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

        self.instructions = instructions
        self.programs = ['a','b','c','d','e','f','g','h','i','j','k', 'l', 'm', 'n', 'o', 'p']
        #import pdb; pdb.set_trace()
        BOUND = 1000*1000*1000
        k = 1
        seen_order = dict()
        while k <= BOUND:
            self.dance()

            str_programs = "".join(self.programs)
            if str_programs in seen_order:
                #import pdb; pdb.set_trace()
                break

            else :
                seen_order[str_programs] = k
                k += 1


        remaining_loop = (BOUND - k) % (k - seen_order[str_programs])
        for i in range(remaining_loop):
            self.dance()
        
        return "".join(self.programs)


    def dance(self):
        """
        one instruction is a dict : 
        {
            "moves" : {'x','s','p'},
            "arg1" : {[0-15],[a-p]},
            "arg2" (optional) : {[0-15],[a-p]}
        }
        """ 
        for instruction in self.instructions:
            if instruction["moves"] == 's':
                i = int(instruction["arg1"])
                self.programs = self.programs[-i:] + self.programs[:16-i]
            
            elif instruction["moves"] == 'x':
                i = int(instruction["arg1"])
                j = int(instruction["arg2"])
                temp = self.programs[i]
                self.programs[i] = self.programs[j]
                self.programs[j] = temp
            
            elif instruction["moves"] == "p":
                a = instruction["arg1"]
                b = instruction["arg2"]
                i = self.programs.index(a)
                j = self.programs.index(b)
                self.programs[i] = b
                self.programs[j] = a
