from submission import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        banks = [int(x) for x in s.split()]
        counter = 0
        seen = set()
        while tuple(banks) not in seen:
            counter += 1
            seen.add(tuple(banks))
            max_index = banks.index(max(banks))
            value = banks[max_index]
            banks[max_index] = 0
            i = 1
            while value > 0:
                banks[(max_index + i) % len(banks)] += 1
                value -= 1
                i += 1
        return counter
