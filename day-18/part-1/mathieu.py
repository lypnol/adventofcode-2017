from runners.python import Submission


class MathieuSubmission(Submission):
    """J'ai repris l'accès aux variables par dictionnaire de Loïc du jour 8"""
    

    def run(self, s):
        instructions = [x.split() for x in s.split('\n')]
        last_snd = None
        current_pos = 0
        registers = {}

        def get(var):
            if var not in registers:
                try:
                    return int(var)
                except:
                    registers[var] = 0
                    return 0
            return registers[var]

        while True:
            data = instructions[current_pos]
            if data[0] == "jgz":
                if get(data[1]) > 0:
                    current_pos += get(data[2])
                    continue
            elif data[0] == "set":
                registers[data[1]] = get(data[2])
            elif data[0] == "add":
                registers[data[1]] = get(data[1]) + get(data[2])
            elif data[0] == "mul":
                registers[data[1]] = get(data[1]) * get(data[2])
            elif data[0] == "mod":
                registers[data[1]] = get(data[1]) % get(data[2])
            elif data[0] == "snd":  # rcv
                last_snd = get(data[1])
            else:  # rcv
                if get(data[1]) > 0:
                    return last_snd
            current_pos += 1

