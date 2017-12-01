from submission import Submission


class ChloeSubmission(Submission):

    def run(self, s):
        jump = int(len(s)/2)
        variable = s + s[:jump]
        total_sum = 0

        for digit_index in range(0,len(s)):
            if variable[digit_index] == variable[digit_index + jump]:
                total_sum += int(variable[digit_index])

        return total_sum