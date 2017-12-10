from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        lengths = list(int(x) for x in s.split(','))
        n = 256
        numbers = list(range(n))
        current_pos = 0
        skip_size = 0
        for length in lengths:
            if current_pos + length < n:
                sublist = numbers[current_pos:current_pos + length]
                numbers = numbers[:current_pos] + list(reversed(sublist)) + numbers[current_pos + length:]
            else:
                sublist = (numbers[current_pos:] + numbers[:current_pos + length - n])
                new_numbers = list(reversed(sublist))[n - current_pos:]
                new_numbers += numbers[current_pos + length - n:current_pos]
                new_numbers += list(reversed(sublist))[:n - current_pos]
                numbers = new_numbers

            current_pos = (current_pos+length + skip_size) % n
            skip_size += 1
        return numbers[0] * numbers[1]
