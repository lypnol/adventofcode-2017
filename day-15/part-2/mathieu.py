from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        start_a = int(s.split("\n")[0].replace("Generator A starts with ", ""))
        start_b = int(s.split("\n")[1].replace("Generator B starts with ", ""))
        count = 0
        for val_a, val_b in self.generator(start_a, start_b):
            bin_a = bin(val_a)[2:].zfill(32)[16:]
            bin_b = bin(val_b)[2:].zfill(32)[16:]
            if bin_a == bin_b:
                count += 1
        return count

    def generator(self, start_a, start_b):
        pairs = 0
        val_a = start_a
        val_b = start_b
        while pairs < 5000000:
            val_a = self.next_a(val_a)
            val_b = self.next_b(val_b)
            pairs += 1
            yield val_a, val_b

    def next_a(self, val_a):
        new_a = (val_a * 16807) % 2147483647
        while new_a % 4:
            new_a = (new_a * 16807) % 2147483647
        return new_a

    def next_b(self, val_b):
        new_b = (val_b * 48271) % 2147483647
        while new_b % 8:
            new_b = (new_b * 48271) % 2147483647
        return new_b