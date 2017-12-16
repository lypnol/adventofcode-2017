from runners.python import Submission


class MathieuSubmission(Submission):
    def __init__(self):
        super().__init__()
        self.n = 0
        self.dance_moves = None

    def run(self, s):
        self.dance_moves = self.read_inputs(s)
        self.n = 16
        group_0 = [chr(97 + i) for i in range(self.n)]
        group = self.one_loop([chr(97 + i) for i in range(self.n)])

        count = 1
        while group != group_0:
            group = self.one_loop(group)
            count += 1
        loops = 1000000000 % count
        count = 0
        while count < loops:
            group = self.one_loop(group)
            count += 1
        return ''.join(group)

    def one_loop(self, group):
        for instruction, elem1, elem2 in self.dance_moves:
            if instruction == "s":
                group = group[self.n - elem1:] + group[:self.n - elem1]
            elif instruction == "x":
                buffer = group[elem1]
                group[elem1], group[elem2] = group[elem2], buffer
            else:  # p
                pos1, pos2 = group.index(elem1), group.index(elem2)
                group[pos1], group[pos2] = elem2, elem1
        return group

    def read_inputs(self, s):
        inputs = s.split(',')
        ret = list()
        for instruction in inputs:
            inst = instruction[0]
            if inst == "s":
                ret.append((inst, int(instruction[1:]), None))
            elif inst == "x":
                pos1, pos2 = map(int, instruction[1:].split("/"))
                ret.append((inst, pos1, pos2))
            else:
                pgm1, pgm2 = instruction[1:].split('/')
                ret.append((inst, pgm1, pgm2))

        return ret
