from runners.python import Submission
from functools import reduce
from itertools import product


class MathieuSubmission(Submission):
    @staticmethod
    def knot_hash_bin(s):
        lengths = list(map(ord,s)) + [17, 31, 73, 47, 23]
        n = 256
        numbers = list(range(n))
        rounds = 64
        round_nb = 0
        current_pos = 0
        skip_size = 0
        while round_nb < rounds:
            for length in lengths:
                if current_pos + length < n:
                    sublist = numbers[current_pos:current_pos + length]
                    sublist.reverse()
                    numbers = numbers[:current_pos] + sublist + numbers[current_pos + length:]
                else:
                    sublist = (numbers[current_pos:] + numbers[:current_pos + length - n])
                    sublist.reverse()
                    numbers = sublist[n - current_pos:] + numbers[current_pos + length - n:current_pos] +sublist[:n - current_pos]

                current_pos = (current_pos + length + skip_size) % n
                skip_size += 1
            round_nb += 1

        dense_hashes = [reduce(lambda x, y: x ^ y, numbers[16 * i:16 * (i + 1)]) for i in range(16)]
        return ''.join(map(lambda x: bin(x)[2:].zfill(8), dense_hashes))

    @staticmethod
    def neighbours(square):
        i_sq, j_sq = square
        return set((i_sq + d_i, j_sq + d_j) for (d_i, d_j) in [(1, 0), (0, 1), (-1, 0), (0, -1)])



    def run(self, s):
        n = 128
        to_visit = set()
        for i in range(n):
            input_key = s + "-" + str(i)
            output_hash = self.knot_hash_bin(input_key)
            for j, char in enumerate(output_hash):
                if char == "1":
                    to_visit.add((i, j))

        count_region = 0
        while to_visit:
            count_region += 1
            to_visit_region = set()
            square = to_visit.pop()
            for neighbour in self.neighbours(square):
                if neighbour in to_visit:
                    to_visit_region.add(neighbour)
                    to_visit.remove(neighbour)
            while to_visit_region:
                square = to_visit_region.pop()
                for neighbour in self.neighbours(square):
                    if neighbour in to_visit:
                        to_visit_region.add(neighbour)
                        to_visit.remove(neighbour)



        return count_region
