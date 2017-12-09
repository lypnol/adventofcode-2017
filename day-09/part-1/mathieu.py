from submission import Submission

class MathieuSubmission(Submission):
    def run(self, s):
        total_score = 0
        group_level = 0
        in_garbage = False
        exclamation_before = False
        for char in s:
            if in_garbage:
                if exclamation_before:
                    exclamation_before = False
                elif char == "!":
                    exclamation_before = True
                else:
                    if char == ">":
                        in_garbage = False
            else:
                if char == "<":
                    in_garbage = True
                elif char == "{":
                    group_level += 1
                elif char == "}":
                    total_score += group_level
                    group_level -= 1

        return total_score

