from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        instructions = []
        registers = {}
        for line in s.split("\n"):
            parts = line.split()
            instructions.append({
                "register" : parts[0],
                "command" : parts[1],
                "offset" : int(parts[2]),
                "condition" : " ".join(parts[4:])
            })
            registers[parts[0]] = 0
        
        highest_value = 0
        for instruction in instructions:
            if self.check_condition(instruction["condition"], registers) :#Check condition
                if instruction["command"] == "inc":
                    registers[instruction["register"]] += instruction["offset"]
                if instruction["command"] == "dec":
                    registers[instruction["register"]] -= instruction["offset"]
            highest_value = max(highest_value, registers[instruction["register"]])

        return highest_value

    def check_condition(self, c, registers):
        parts = c.split()
        assert(len(parts) == 3)
        if parts[1] == '<':
            return registers[parts[0]] < int(parts[2])
        if parts[1] == '>':
            return registers[parts[0]] > int(parts[2])
        if parts[1] == '<=':
            return registers[parts[0]] <= int(parts[2])
        if parts[1] == '>=':
            return registers[parts[0]] >= int(parts[2])
        if parts[1] == '==':
            return registers[parts[0]] == int(parts[2])
        if parts[1] == '!=':
            return registers[parts[0]] != int(parts[2])
