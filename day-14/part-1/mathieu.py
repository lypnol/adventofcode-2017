from runners.python import Submission
from functools import reduce


class MathieuSubmission(Submission):

    @staticmethod
    def knot_hash(s):
        lengths = list(ord(x) for x in s) + [17, 31, 73, 47, 23]
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

        return ''.join(map(lambda x: hex(x)[2:].zfill(2), dense_hashes))

    def run(self, s):
        n = 128
        square_used = 0
        for i in range(n):
            input_key = s + "-" + str(i)
            output_hash = self.knot_hash(input_key)
            square_used += bin(int(output_hash, 16))[:2].count("1")
        return square_used
