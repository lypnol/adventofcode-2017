from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        variables=dict()
        inputs=[line.split() for line in s.split('\n')]
        for line in inputs:
            var = line[4]
            if var not in variables:
                variables[var] = 0

            condition = "variables['" + line[4] + "'] "
            condition += line[5] + " " + line[6]
            if eval(condition):

                var=line[0]
                if var not in variables:
                    variables[var] = 0

                execution = "variables['" + line[0] + "']"
                execution += " += " if line[1] == "inc" else " -= "
                execution+=line[2]
                exec(execution)

        return max(variables.values())
