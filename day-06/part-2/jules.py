import hashlib
from submission import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        banks = [int(x) for x in s.split()]
        counter = 0
        seen = []
        while hashlib.blake2b(''.join([str(x) for x in banks]).encode('utf-8')).hexdigest() not in seen:
            counter += 1
            seen.append(hashlib.blake2b(''.join([str(x) for x in banks]).encode('utf-8')).hexdigest())
            max_index = banks.index(max(banks))
            value = banks[max_index]
            banks[max_index] = 0
            i = 1
            while value > 0:
                banks[(max_index + i) % len(banks)] += 1
                value -= 1
                i += 1
        return counter - seen.index(hashlib.blake2b(''.join([str(x) for x in banks]).encode('utf-8')).hexdigest())
