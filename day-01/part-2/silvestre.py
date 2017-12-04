from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        """
        :param s: input in string format
        :return: solution in integer format
        """
        result = 0
        char_list = list(s)
        half_len = int((len(char_list))/2)
        sublist_1 = char_list[:half_len]
        sublist_2 = char_list[half_len:]
        for i, char in enumerate(sublist_1):
            if char == sublist_2[i]:
                result += int(char)
        for i, char in enumerate(sublist_2):
            if char == char_list[i]:
                result += int(char)
        return result
