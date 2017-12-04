from enum import Enum
from submission import Submission


class JulesSubmission(Submission):

    def run(self, s):
        class Direction(Enum):
            UP = 0
            LEFT = 1
            DOWN = 2
            RIGHT = 3
        # :param s: input in string format
        # :return: solution flag
        # your solution code goes here
        matrix = {(0, 0): 1}
        direction = Direction.UP
        position = (1, 0)
        number = 1
        while number < int(s):
            x, y = position
            neighbors = [(x - 1, y), (x - 1, y - 1), (x - 1, y + 1),
                         (x, y + 1), (x, y - 1), (x + 1, y - 1),
                         (x + 1, y), (x + 1, y + 1)]
            number = sum([matrix[nb] for nb in neighbors if nb in matrix])
            matrix[position] = number
            if direction == Direction.RIGHT:
                position = (x + 1, y)
                if (position[0], position[1] + 1) not in matrix:
                    direction = Direction.UP
            elif direction == Direction.LEFT:
                position = (x - 1, y)
                if (position[0], position[1] - 1) not in matrix:
                    direction = Direction.DOWN
            elif direction == Direction.UP:
                position = (x, y + 1)
                if (position[0] - 1, position[1]) not in matrix:
                    direction = Direction.LEFT
            elif direction == Direction.DOWN:
                position = (x, y - 1)
                if (position[0] + 1, position[1]) not in matrix:
                    direction = Direction.RIGHT
        return number
