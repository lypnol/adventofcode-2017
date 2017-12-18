from runners.python import Submission


class MathieuSubmission(Submission):
    """J'ai repris l'accès aux variables par dictionnaire de Loïc du jour 8"""
    count_send_1 = 0
    blocked_1 = False
    blocked_0 = False
    inbox_0 = []
    inbox_1 = []

    def run(self, s):
        self.instructions = [x.split() for x in s.split('\n')]
        current_pos_0, current_pos_1 = 0, 0
        registers_0, registers_1 = {'p': 0}, {'p': 1}
        while not (self.blocked_0 and self.blocked_1):
            current_pos_0, registers_0 = self.execute_instruction(current_pos_0, registers_0, 0)
            current_pos_1, registers_1 = self.execute_instruction(current_pos_1, registers_1, 1)

        return self.count_send_1

    def get(self, registers, var):
        if var not in registers:
            try:
                return int(var)
            except:
                registers[var] = 0
                return 0
        return registers[var]

    def execute_instruction(self, current_pos, registers, id):
        data = self.instructions[current_pos]
        if data[0] == "jgz":
            if self.get(registers, data[1]) > 0:
                current_pos += self.get(registers, data[2])
                return current_pos, registers
        elif data[0] == "set":
            registers[data[1]] = self.get(registers, data[2])
        elif data[0] == "add":
            registers[data[1]] = self.get(registers, data[1]) + self.get(registers, data[2])
        elif data[0] == "mul":
            registers[data[1]] = self.get(registers, data[1]) * self.get(registers, data[2])
        elif data[0] == "mod":
            registers[data[1]] = self.get(registers, data[1]) % self.get(registers, data[2])
        elif data[0] == "snd":
            if id:
                self.inbox_0.append(self.get(registers, data[1]))
                self.count_send_1 += 1
            else:
                self.inbox_1.append(self.get(registers, data[1]))
        else:  # rcv
            if id == 0 and self.inbox_0 == []:
                self.blocked_0 = True
                return current_pos, registers
            elif id == 0:
                self.blocked_0 = False
                registers[data[1]] = self.inbox_0.pop(0)
            elif not self.inbox_1:
                self.blocked_1 = True
                return current_pos, registers
            else:
                self.blocked_1 = False
                registers[data[1]] = self.inbox_1.pop(0)

        current_pos += 1
        return current_pos, registers
