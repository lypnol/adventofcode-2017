from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        """
        :param s: input in string format
        :return: solution in integer format
        """
        result = 0
        char_list = list(s)
        char_list.append(char_list[0])
        for i, char in enumerate(char_list[:-1]):
            if char == char_list[i+1]:
                result += int(char)
        return result
