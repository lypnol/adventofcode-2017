from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        list_size = 256
        num_list = [x for x in range(list_size)]
        pos = 0
        skip = 0
        # s = '3, 4, 1, 5'
        size_list = [int(x) for x in s.split(',')]
        for size in size_list:
            # new_list = list_size[position:position+int(size)][::-1] +
            new_list = num_list[:]
            for el in range(size // 2):
                # print((pos + el) % list_size, (pos + size - 1 - el) % list_size)
                new_list[(pos + el) %
                         list_size] = num_list[(pos + size - 1 - el) % list_size]
                new_list[(pos + size - 1 - el) %
                         list_size] = num_list[(pos + el) % list_size]
            num_list = new_list[:]
            pos = (pos + size + skip) % list_size
            skip += 1
            # print(num_list, pos)
        return num_list[0] * num_list[1]
