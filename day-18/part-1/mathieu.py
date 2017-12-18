from runners.python import Submission


class MathieuSubmission(Submission):
    """J'ai repris l'accès aux variables par dictionnaire de Loïc du jour 8"""
    registers = {}

    def run(self, s):
        instructions = [x.split() for x in s.split('\n')]
        last_snd = None
        current_pos = 0
        while True:
            data = instructions[current_pos]

            if data[0] == "jgz":
                if self.get(data[1]) > 0:
                    current_pos += self.get(data[2])
                else:
                    current_pos += 1
                continue
            elif data[0] == "set":
                self.registers[data[1]] = self.get(data[2])
            elif data[0] == "add":
                self.registers[data[1]] = self.get(data[1]) + self.get(data[2])
            elif data[0] == "mul":
                self.registers[data[1]] = self.get(data[1]) * self.get(data[2])
            elif data[0] == "mod":
                self.registers[data[1]] = self.get(data[1]) % self.get(data[2])
            elif data[0] == "snd":  # rcv
                last_snd = self.get(data[1])
            else:  # rcv
                if self.get(data[1]) > 0:
                    return last_snd
            current_pos += 1

    def get(self, var):
        if var not in self.registers:
            try:
                return int(var)
            except:
                self.registers[var] = 0
                return 0
        return self.registers[var]

