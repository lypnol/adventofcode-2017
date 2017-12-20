from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        lines = s.split('\n')
        top = lines[0].index('|'), 0
        go_right, go_left = False, False
        go_up, go_down = False, True
        i = 0
        previous_plus_pos = top
        current_pos = top[0], top[1] + i
        current_char = lines[top[1] + i][top[0]]
        path = ""
        while True:
            i += 1
            if go_right:
                if previous_plus_pos[0] + i >= len(lines[0]):
                    break
                current_char = lines[previous_plus_pos[1]][previous_plus_pos[0] + i]
                current_pos = previous_plus_pos[0] + i, previous_plus_pos[1]
            elif go_left:
                if previous_plus_pos[0] - i < 0:
                    break
                current_char = lines[previous_plus_pos[1]][previous_plus_pos[0] - i]
                current_pos = previous_plus_pos[0] - i, previous_plus_pos[1]
            elif go_up:
                if previous_plus_pos[1] - i < 0:
                    break
                current_char = lines[previous_plus_pos[1] - i][previous_plus_pos[0]]
                current_pos = previous_plus_pos[0], previous_plus_pos[1] - i
            elif go_down:
                if previous_plus_pos[1] + i >= len(lines):
                    break
                current_char = lines[previous_plus_pos[1] + i][previous_plus_pos[0]]
                current_pos = previous_plus_pos[0], previous_plus_pos[1] + i
            if current_char == ' ':
                break
            elif current_char not in {'|', '+', '-'}:
                path += current_char
            elif current_char == "+":
                previous_plus_pos = current_pos
                current_char = ""
                i = 0
                if go_down or go_up:
                    if lines[previous_plus_pos[1]][previous_plus_pos[0] - 1] != " ":
                        go_down = go_up = go_right = False
                        go_left = True
                    else:
                        go_down = go_up = go_left = False
                        go_right = True
                else:
                    if lines[previous_plus_pos[1] - 1][previous_plus_pos[0]] != " ":
                        go_left = go_right = go_down = False
                        go_up = True
                    else:
                        go_left = go_right = go_up = False
                        go_down = True
        return path
