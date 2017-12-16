from runners.python import Submission


class MathieuSubmission(Submission):
    def __init__(self):
        super().__init__()
        self.n = 0
        self.dance_moves = None

    def run(self, s):
        self.dance_moves = s.split(",")
        self.n = 16
        group = self.one_loop([chr(97 + i) for i in range(self.n)])
        return ''.join(group)

    def one_loop(self, group):
        for dance_move in self.dance_moves:
            instruction = dance_move[0]
            if instruction == "s":
                spin_size = int(dance_move[1:])
                group = group[self.n - spin_size:] + group[:self.n - spin_size]
            elif instruction == "x":
                pos1, pos2 = map(int, dance_move[1:].split("/"))
                buffer = group[pos1]
                group[pos1], group[pos2] = group[pos2], buffer
            else:  # p
                pgm1, pgm2 = dance_move[1:].split('/')
                pos1, pos2 = group.index(pgm1), group.index(pgm2)
                group[pos1], group[pos2] = pgm2, pgm1
        return group
