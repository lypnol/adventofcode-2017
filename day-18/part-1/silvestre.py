from collections import defaultdict
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        instructions = self.read_input(s)
        registers = defaultdict(int)
        
        last_sound_played = 0
        first_sound_recovered = False
        i = 0  # index de curr dans instructions
        while not first_sound_recovered:
            curr = instructions[i]
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
            if cmd == "jgz" and x_val >= 0:
                i = i + y_val
                continue
            if cmd == "snd":
                last_sound_played = x_val
            elif cmd == "set":
                registers[x] = y_val
            elif cmd == "add":
                registers[x] = x_val + y_val
            elif cmd == "mul":
                registers[x] = x_val * y_val
            elif cmd == "mod":
                registers[x] = x_val % y_val
            elif cmd == "rcv":
                first_sound_recovered = True

            i += 1

        return last_sound_played

    def read_input(self, s):
        inputs = s.split("\n")
        instructions = list()
        for row in inputs:
            rl = row.split()
            if len(rl)==2:
                instructions.append((rl[0], rl[1], None))
            else:
                instructions.append((rl[0], rl[1], rl[2]))
        return instructions
