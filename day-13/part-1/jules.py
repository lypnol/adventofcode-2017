from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # curr_round = 0
        firewall = {}
        score = 0
        for definition in s.split('\n'):
            u, v = definition.split(': ')
            firewall[int(u)] = int(v)

        max_depth = max(firewall.keys())
        for curr_round in range(max_depth + 1):
            if curr_round in firewall:
                if curr_round % (firewall[curr_round] * 2 - 2) == 0:
                    score += curr_round * firewall[curr_round]

        return score
