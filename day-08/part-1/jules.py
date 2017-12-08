from submission import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        my_vars = dict()
        for line in s.split('\n'):
            splitted = line.split()
            variables = [splitted[0], splitted[4]]
            for var in variables:
                if var not in my_vars:
                    my_vars[var] = 0
            if splitted[5] == '!=':
                if my_vars[splitted[4]] == int(splitted[6]):
                    continue
            elif splitted[5] == '==':
                if my_vars[splitted[4]] != int(splitted[6]):
                    continue
            elif splitted[5] == '>=':
                if my_vars[splitted[4]] < int(splitted[6]):
                    continue
            elif splitted[5] == '>':
                if my_vars[splitted[4]] <= int(splitted[6]):
                    continue
            elif splitted[5] == '<=':
                if my_vars[splitted[4]] > int(splitted[6]):
                    continue
            elif splitted[5] == '<':
                if my_vars[splitted[4]] >= int(splitted[6]):
                    continue
            else:
                print("Unknown comparison")
            if splitted[1] == 'inc':
                my_vars[splitted[0]] += int(splitted[2])
            elif splitted[1] == 'dec':
                my_vars[splitted[0]] -= int(splitted[2])
            else:
                print("Operator unknown")
        return max(my_vars.values())
