from runners.python import Submission
from functools import reduce


class MathieuSubmission(Submission):
    def run(self, s):
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
                    numbers = numbers[:current_pos] + list(reversed(sublist)) + numbers[current_pos + length:]
                else:
                    sublist = (numbers[current_pos:] + numbers[:current_pos + length - n])
                    new_numbers = list(reversed(sublist))[n - current_pos:]
                    new_numbers += numbers[current_pos + length - n:current_pos]
                    new_numbers += list(reversed(sublist))[:n - current_pos]
                    numbers = new_numbers

                current_pos = (current_pos + length + skip_size) % n
                skip_size += 1
            round_nb += 1

        dense_hashes = [reduce(lambda x, y: x ^ y, numbers[16 * i:16 * (i + 1)]) for i in range(16)]

        return ''.join(map(lambda x: hex(x)[2:].zfill(2), dense_hashes))
