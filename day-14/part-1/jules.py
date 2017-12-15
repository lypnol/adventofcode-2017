from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
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
        return sum([bin(int(knot_hash('{}-{}'.format(s, i)), 16)).count('1') for i in range(128)])