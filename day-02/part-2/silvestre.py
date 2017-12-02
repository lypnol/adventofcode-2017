from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        table_str = [row.split("\t") for row in s.split("\n")]
        table_int = [list(map(int, row)) for row in table_str]
        result = 0
        return sum(self.get_row_result(row) for row in table_int)

    def get_row_result(self, row):
        # :param row: list of integers
        # :return: solution
        row_result = 0
        for i, value in enumerate(row):
            row_result += sum(value//value2 if value % value2 == 0 and i != j else 0 for j, value2 in enumerate(row))
        return row_result
