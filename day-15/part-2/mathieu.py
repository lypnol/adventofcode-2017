from runners.python import Submission


class MathieuSubmission(Submission):
    """j'ai refait la comparaison entre a et b, en m'inspirant des algos de Jules et David
    Mon algo était vraiment trop long sinon..."""
    def run(self, s):
        start_a = int(s.split("\n")[0].replace("Generator A starts with ", ""))
        start_b = int(s.split("\n")[1].replace("Generator B starts with ", ""))
        count = 0
        for val_a, val_b in self.generator(start_a, start_b):
            if (val_a - val_b) & 0xffff==0:
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
