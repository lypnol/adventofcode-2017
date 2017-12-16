from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        instructions = s.split(',')
        state = [chr(i) for i in range(ord('a'), ord('p') + 1)]

        for instruction in instructions:
            if instruction[0] == 's':
                offset = int(instruction[1:])
                state = state[-offset:] + state[:-offset]
            elif instruction[0] == 'x':
                numbers = [int(x) for x in instruction[1:].split('/')]
                temp = state[numbers[0]]
                state[numbers[0]] = state[numbers[1]]
                state[numbers[1]] = temp
            elif instruction[0] == 'p':
                programs = (instruction[1], instruction[3])
                pos = (state.index(programs[0]), state.index(programs[1]))
                temp = state[pos[0]]
                state[pos[0]] = state[pos[1]]
                state[pos[1]] = temp
        return "".join(state)
