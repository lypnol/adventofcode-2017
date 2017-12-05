from submission import Submission


class JulesSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        def find_for_row(row):
            for fi in range(len(row)):
                for si in range(fi + 1, len(row)):
                    if row[fi] > row[si] and row[fi] % row[si] == 0:
                        return int(row[fi] / row[si])
                    elif row[si] % row[fi] == 0:
                        return int(row[si] / row[fi])

        row_list = [[int(x) for x in row.split()] for row in s.split('\n')]
        return str(sum([find_for_row(row) for row in row_list]))
