from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        garbage = False
        after_exclamation = False
        curr_score = 0
        score = 0
        for char in s:
            if after_exclamation:
                after_exclamation = False
                continue
            elif garbage and char == '!':
                after_exclamation = True
                continue
            elif garbage and char != '>':
                continue
            elif garbage and char == '>':
                garbage = False
            elif char == '{':
                curr_score += 1
                continue
            elif char == '}':
                score += curr_score
                curr_score -= 1
                continue
            elif char == '<':
                garbage = True
        return score
