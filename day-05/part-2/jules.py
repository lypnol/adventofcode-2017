from submission import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        offset = 0
        instructions = [int(x) for x in s.split('\n')]
        length = len(instructions)
        counter = 0
        while 0 <= offset < length:
            counter += 1
            old_offset = offset
            offset += instructions[offset]
            if instructions[old_offset] >= 3:
                instructions[old_offset] -= 1
            else:
                instructions[old_offset] += 1
        return counter
