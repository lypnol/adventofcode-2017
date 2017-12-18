from collections import defaultdict, deque
from submission import Submission


class SilvestreSubmission(Submission):
    """
    Inspiré fortement de ce qu'a fait Mathieu (les threads j'ai pas compris)
    """

    def run(self, s):
        instructions = self.read_input(s)
        self.count_sent_1 = 0
        self.blocked_0 = False
        self.blocked_1 = False

        current_pos_0, current_pos_1 = 0, 0
        registers_0 = defaultdict(int)
        registers_1 = defaultdict(int)
        registers_1['p'] = 1

        self.queue_0 = deque()
        self.queue_1 = deque()

        while not (self.blocked_0 and self.blocked_1):
            current_pos_0, registers_0 = self.execute_instruction(instructions, current_pos_0, registers_0, 0)
            current_pos_1, registers_1 = self.execute_instruction(instructions, current_pos_1, registers_1, 1)

        return self.count_sent_1

    def execute_instruction(self, instructions, current_pos, registers, prog_id):
        curr = instructions[current_pos]
        cmd, x, y = curr

        try:
            x_val = int(x)
        except ValueError:
            x_val = registers[x]
        try:
            y_val = int(y)
        except ValueError:
            y_val = registers[y]
        except TypeError:
            pass

        if cmd == "jgz" and x_val > 0:
            return current_pos + y_val, registers
        elif cmd == "snd":
            if prog_id:
                self.queue_0.append(x_val)
                self.count_sent_1 += 1
            else:
                self.queue_1.append(x_val)
        elif cmd == "set":
            registers[x] = y_val
        elif cmd == "add":
            registers[x] = x_val + y_val
        elif cmd == "mul":
            registers[x] = x_val * y_val
        elif cmd == "mod":
            registers[x] = x_val % y_val
        elif cmd == "rcv":
            if prog_id and self.queue_1:
                self.blocked_1 = False
                registers[x] = self.queue_1.popleft()
            elif prog_id:
                self.blocked_1 = True
                return current_pos, registers
            elif not prog_id and self.queue_0:
                self.blocked_0 = False
                registers[x] = self.queue_0.popleft()
            else:
                self.blocked_0 = True
                return current_pos, registers
        
        current_pos += 1
        return current_pos, registers

    def read_input(self, s):
        instructions = [row.split() for row in s.split("\n")]
        for instruction in instructions:
            if len(instruction) == 2:
                instruction.append(None)
        return instructions