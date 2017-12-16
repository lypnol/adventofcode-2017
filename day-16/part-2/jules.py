from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        instructions = s.split(',')
        state = [chr(i) for i in range(ord('a'), ord('p') + 1)]
        i = 0
        states_dict = {}
        rounds = 1000000000
        while i < rounds:
            begin_state = tuple(state)
            if begin_state in states_dict:
                number_of_rounds = i - states_dict[begin_state]
                remaining_rounds = (rounds - i)
                i = rounds - (remaining_rounds % number_of_rounds)
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
            states_dict[begin_state] = i
            i += 1
        return "".join(state)
