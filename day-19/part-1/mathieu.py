import re
from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        start, stop, pluses, letters = self.read_inputs(s)
        print(start, stop, pluses, letters)
        horizontal_move = False
        current_plus = start
        x_pos, y_pos = current_plus
        x_mov, y_move = 0, 0
        path = ""
        nb_plus = 0
        while nb_plus < len(pluses) - 1:
            if horizontal_move:
                if x_mov:
                    next_plus = min({plus for plus in pluses.keys() if plus[0] > x_pos and plus[1] == y_pos},
                                    key=lambda plus: plus[1])  # is on the left
                else:
                    next_plus = max({plus for plus in pluses.keys() if plus[0] < x_pos and plus[1] == y_pos},
                                    key=lambda plus: plus[1])  # is on the right
            else:
                if y_move:
                    next_plus = max({plus for plus in pluses.keys() if plus[0] == x_pos and plus[1] < y_pos},
                                    key=lambda plus: plus[1])  # is above
                else:
                    next_plus = min({plus for plus in pluses.keys() if plus[0] == x_pos and plus[1] > y_pos},
                                    key=lambda plus: plus[1])  # is below
            path = self.add_letter_between(current_plus, next_plus, letters, path)
            nb_plus += 1
            current_plus = next_plus
            x_pos, y_pos = current_plus
            x_mov, y_move = pluses[current_plus]
            horizontal_move = not horizontal_move
            print(current_plus)
        print(stop)
        path = self.add_letter_between(current_plus, stop, letters, path)
        print(path)

    def read_inputs(self, s):
        inputs = s.split('\n')
        start = (inputs[0].index('|'), 0)
        stop = None
        pluses = {start: (0, 0)}
        letters = {}
        active_vertical_lines = {start[0]}
        for y_plus, line in enumerate(inputs):
            e = True
            x_pluses = [x for x, char in enumerate(line) if char == '+']
            for x_plus in x_pluses:
                if x_plus in active_vertical_lines:
                    active_vertical_lines.remove(x_plus)
                    pluses[(x_plus, y_plus)] = (e, 1)
                else:
                    pluses[(x_plus, y_plus)] = (e, 0)
                    active_vertical_lines.add(x_plus)
                e = not e
            x_letters = {x for x, char in enumerate(line) if char not in {' ', '|', '+', '-'}}
            for x_letter in x_letters:
                letters[(x_letter, y_plus)] = line[x_letter]
                if (x_letter == len(line) - 2 or x_letter == 1 or y_plus == len(inputs) - 2) \
                        and len({plus for plus in pluses if plus[0] == x_letter or plus[1] == y_plus}) % 2 == 1:
                    stop = (x_letter, y_plus)

        return start, stop, pluses, letters

    def add_letter_between(self, plus_1, plus_2, letters, path):
        letters_between = list(filter(
            lambda letter: min(plus_1[0], plus_2[0]) <= letter[0] <= max(plus_1[0], plus_2[0])
                           and min(plus_1[1], plus_2[1]) <= letter[1] <= max(plus_1[1], plus_2[1]), letters))
        if letters_between:
            if plus_1[0] <= plus_2[0] and plus_1[1] <= plus_2[1]:
                path += "".join(map(lambda let: letters[let], sorted(letters_between, key=lambda x: x[0] + x[1])))
            else:
                path += "".join(
                    map(lambda let: letters[let], sorted(letters_between, key=lambda x: x[0] + x[1], reverse=True)))
        return path

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
            if current_char not in {' ', '|', '+', '-'}:
                path += current_char
            if current_char == "+":
                previous_plus_pos = current_pos
                current_char = ""
                i = 0
                if go_down or go_up:
                    if lines[previous_plus_pos[1]][previous_plus_pos[0] - 1] != " ":
                        go_down, go_up = False, False
                        go_left, go_right = True, False
                    else:
                        go_down, go_up = False, False
                        go_left, go_right = False, True
                else:
                    if lines[previous_plus_pos[1] - 1][previous_plus_pos[0]] != " ":
                        go_down, go_up = False, True
                        go_left, go_right = False, False
                    else:
                        go_down, go_up = True, False
                        go_left, go_right = False, False
        return path
