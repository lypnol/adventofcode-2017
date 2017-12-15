from runners.python import Submission

SIZE = 128


class JulesSubmission(Submission):

    def run(self, s):
        self.visited = [[False for i in range(SIZE)] for j in range(SIZE)]
        self.grid = []
        def knot_hash(s, rounds=64):
            list_size = 256
            num_list = [x for x in range(list_size)]
            pos = 0
            skip = 0
            size_list = [ord(x) for x in s] + [17, 31, 73, 47, 23]
            for i in range(rounds):
                for size in size_list:
                    new_list = num_list[:]
                    for el in range(size // 2):
                        new_list[(pos + el) %
                                 list_size] = num_list[(pos + size - 1 - el) % list_size]
                        new_list[(pos + size - 1 - el) %
                                 list_size] = num_list[(pos + el) % list_size]
                    num_list = new_list[:]
                    pos = (pos + size + skip) % list_size
                    skip += 1
            final = [0] * 16
            for block in range(16):
                for i in range(16):
                    final[block] ^= num_list[16 * block + i]
            return ''.join(["%02x" % (i) for i in final])

        def BFS(i, j):
            def not_visited(i, j):
                return (i >= 0 and i < SIZE and j >= 0 and j < SIZE and not self.visited[i][j] and self.grid[i][j] == '1')
            to_visit = set()
            to_visit.add((i, j))
            while len(to_visit) > 0:
                i, j = to_visit.pop()
                self.visited[i][j] = True
                row = [-1, 0, 0, 1]
                col = [0, 1, -1, 0]
                for a in range(4):
                    if not_visited(i + row[a], j + col[a]):
                        to_visit.add((i + row[a], j + col[a]))

        count = 0
        for i in range(SIZE):
            self.grid.append(list("{0:0>128}".format(bin(int(knot_hash('{}-{}'.format(s, i)), 16))[2:])))
        for i in range(SIZE):
            for j in range(SIZE):
                if not self.visited[i][j] and self.grid[i][j] == '1':
                    BFS(i, j)
                    count += 1

        return count
