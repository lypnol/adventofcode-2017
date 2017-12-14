from functools import reduce
from submission import Submission

class SilvestreSubmission(Submission):
    
    def __init__(self, *args, **kwargs):
        self.matrix = []
        self.unvisited = []
    
    def run(self, s):
        self.matrix = []
        for i in range(128):
            self.matrix.append(list("".join([bin(int(c, 16))[2:].zfill(4) for c in self.knot_hashes(f'{s}-{i}')])))
        assert(len(self.matrix)==128)
        assert(len(self.matrix[0])==128)
        self.unvisited = [(x, y) for y in range(128) for x in range(128)]
        count = 0
        while len(self.unvisited) > 0:
            i, j = self.unvisited[0]

            if self.matrix[i][j] == '1':
                count += 1
                self.visit(i,j)
            else:
                self.unvisited.remove((i, j))
        return count
    
    def visit(self, i, j):
        if (i, j) in self.unvisited:
            self.unvisited.remove((i, j))
            if self.matrix[i][j] == '1':
                if j > 0:
                    self.visit(i, j-1)
                if j < 127:
                    self.visit(i, j+1)
                if i > 0:
                    self.visit(i-1, j)
                if i < 127:
                    self.visit(i+1, j)

    def knot_hashes(self, s):
        """
        Copy-Paste of Day-10
        """
        lengths = list(map(ord,s)) + [17, 31, 73, 47, 23]
        main_list = list(range(256))
        
        current_position = 0
        skip_size = 0 
        for i in range(64):    
            for length in lengths:
                i1 = current_position
                i2 = (current_position + length) % 256

                if i1 < i2:
                    sublist = main_list[i1 : i2]
                    sublist.reverse()

                    l1 = main_list[:i1]
                    l2 = main_list[i2:]

                    main_list = l1 +sublist + l2
                elif i1 > i2:
                    sublist = main_list[i1:] + main_list[:i2]
                    assert(len(sublist) == length)
                    sublist.reverse()

                    if i2 != 0:
                        main_list = sublist[-i2:] + main_list[i2:i1] + sublist[:(256-i1)]
                    else :
                        main_list = main_list[i2:i1] + sublist[:(256-i1)]

                current_position = (current_position + length + skip_size) % 256
                skip_size += 1
            
                assert(len(main_list)==256)

        sparse_hash = [main_list[i:i+16] for i in range(0, len(main_list), 16)]

        dense_hash = [reduce(lambda i, j: int(i) ^ int(j), block) for block in sparse_hash]

        final_output = "".join(list(map('{0:02x}'.format,dense_hash)))

        return final_output
            