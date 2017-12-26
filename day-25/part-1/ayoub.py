from runners.python import Submission
from collections import defaultdict
import pprint


class AyoubSubmission(Submission):

    def run(self, s):
        lines = s.split('\n')
        actions = {}
        pause = int(lines[1].split()[5])

        for i in range(2, len(lines), 10):
            desc = lines[i:i+10]
            state = desc[1].split()[2][:-1]
            action = [
                (int(desc[3].split()[4][:-1]), 1 if desc[4].split()[6][:-1] == 'right' else -1, desc[5].split()[4][:-1]),
                (int(desc[7].split()[4][:-1]), 1 if desc[8].split()[6][:-1] == 'right' else -1, desc[9].split()[4][:-1])
            ]
            actions[state] = action
        
        state = lines[0].split()[3][:-1]
        tape = {}
        # pp = pprint.PrettyPrinter(indent=2)
        # pp.pprint(state)
        # pp.pprint(actions)

        cur = 0
        val = 0
        tape[cur] = val
        for _ in range(pause):
            write, move, next_state = actions[state][val]
            tape[cur] = write
            cur += move
            state = next_state
            if cur in tape:
                val = tape[cur]
            else:
                val = 0

        count = 0
        for v in tape.values():
            if v == 1: count += 1
        return count
