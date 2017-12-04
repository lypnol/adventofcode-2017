from submission import Submission


class MathieuSubmission(Submission):

    def add_square(self, grid):

        # 1. Find the new position
        last_x, last_y = list(grid.keys())[-1]
        layer_nb = max(abs(last_x), abs(last_y))

        # 1.1 Vertical move
        if last_x == -layer_nb and last_y == layer_nb:
            new_x = last_x
            new_y = last_y - 1

        elif abs(last_x) == layer_nb and abs(last_y) < layer_nb:
            new_x = last_x
            new_y = last_y + last_x / abs(last_x)

        # 1.2 Horizontal move
        else:
            new_x = last_x - last_y / abs(last_y)
            new_y = last_y

        # 2. Sum values of neighbors
        new_value = 0
        for x, y in grid:
            if abs(new_x - x) < 2 and abs(new_y - y) < 2:
                new_value += grid[(x, y)]
        grid[(new_x, new_y)] = new_value
        return grid, new_value

    def run(self, s):
        target_value = int(s)
        last_value_added = 1

        # We store the grid as a dictionary (x_position, y_position) --> square_value
        grid = dict()
        grid[(0, 0)] = 1
        grid[(1, 0)] = 1
        while last_value_added <= target_value:
            grid, last_value_added = self.add_square(grid)
        return last_value_added
