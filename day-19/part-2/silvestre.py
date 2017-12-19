import re
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        tubes = self.read_input(s)

        steps = 1

        for key in tubes:
            if key[0] == 0:
                curr_i, curr_j = key

        max_i = max(key[0] for key in tubes)
        max_j = max(key[1] for key in tubes)

        """
        Direction :
        0 - descending
        1 - left
        2 - ascending
        3 - right
        """
        direction = 0

        while curr_i >= 0 and curr_j >= 0 and curr_i <= max_i and curr_j <= max_j:
            direction, curr_i, curr_j, steps = self.execute_instructions(tubes, direction, curr_i, curr_j, steps)
        return steps

    def execute_instructions(self, tubes, direction, curr_i, curr_j, steps):
        if direction == 0:
            curr_i += 1
        elif direction == 1:
            curr_j -= 1
        elif direction == 2:
            curr_i -= 1
        else:
            curr_j += 1
        steps += 1
        curr_c = tubes[(curr_i, curr_j)]
        while not curr_c == "+":
            if direction == 0:
                curr_i += 1
            elif direction == 1:
                curr_j -= 1
            elif direction == 2:
                curr_i -= 1
            else:
                curr_j += 1
            if not (curr_i, curr_j) in tubes:
                return 0, -1, -1, steps
            curr_c = tubes[(curr_i, curr_j)]
            steps += 1

        # Une fois qu'on est arrivé au +, on trouve la nouvelle direction
        list_dir_available = []
        if (curr_i+1, curr_j) in tubes:
            if tubes[(curr_i+1, curr_j)] == '|':
                list_dir_available.append(0)
        if (curr_i, curr_j-1) in tubes:
            if tubes[(curr_i, curr_j-1)] == '-':
                list_dir_available.append(1)
        if (curr_i-1, curr_j) in tubes:
            if tubes[(curr_i-1, curr_j)] == '|':
                list_dir_available.append(2)
        if (curr_i, curr_j+1) in tubes:
            if tubes[(curr_i, curr_j+1)] == '-':
                list_dir_available.append(3)
        # On enlève la direction dont on vient
        if (direction + 2) % 4 in list_dir_available:
            list_dir_available.remove((direction + 2) % 4)
        assert(len(list_dir_available) == 1)
        direction = list_dir_available.pop()    

        return direction, curr_i, curr_j, steps

    def read_input(self, s):
        """
        On crée un dictionnaire qui à un tuple (i, j) associe un caractère parmi [-, +, |] ou une lettre
        """
        tubes = {}
        for i, row in enumerate(s.split("\n")):
            for j, car in enumerate(list(row)):
                if not car == " ":
                    assert car in ['-', '+', '|'] or bool(re.match(r'^[A-Z]$', car))
                    tubes[(i, j)] = car

        return tubes
