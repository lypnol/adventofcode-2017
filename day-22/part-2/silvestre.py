from collections import deque
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        current_grid = self.read_input(s)

        virus_pos = [len(current_grid)//2 for i in range(2)]

        burst = 0
        counter = 0
        direction = 0
        while burst < 10000000:
            current_grid, virus_pos, direction, counter = self.execute_burst(current_grid, virus_pos, direction, counter)
            burst += 1
        
        return counter

    def execute_burst(self, current_grid, virus_pos, direction, counter):
        """
        Direction :
        0 - ascending
        1 - right
        2 - descending
        3 - left

        State :
        0 - Clean
        1 - Weakened
        2 - Infected
        3 - Flagged
        """
        # Step 1 & 2
        curr_x = virus_pos[0]
        curr_y = virus_pos[1]
        assert 0 <= curr_x < len(current_grid) and 0 <= curr_y < len(current_grid)
        if current_grid[curr_x][curr_y] == 0:
            direction = (direction - 1) % 4      # Step 1
            current_grid[curr_x][curr_y] = 1    # Step 2
        elif current_grid[curr_x][curr_y] == 1:
            current_grid[curr_x][curr_y] = 2    # Step 2 (pas de step 1)
            counter += 1
        elif current_grid[curr_x][curr_y] == 2:
            direction = (direction + 1) % 4      # Step 1
            current_grid[curr_x][curr_y] = 3    # Step 2
        else:
            direction = (direction + 2) % 4      # Step 1
            current_grid[curr_x][curr_y] = 0    # Step 2
        # Avant d'avancer il faut agrandir la grille si besoin
        grid_dim = len(current_grid)
        if curr_x in [0, grid_dim-1] or curr_y in [0, grid_dim-1]:
            for i in range(grid_dim):
                current_grid[i].appendleft(0)
                current_grid[i].append(0)
            curr_y += 1
            # import pdb; pdb.set_trace()
            current_grid.appendleft(deque(list([0 for i in range(grid_dim+2)])))
            current_grid.append(deque(list([0 for i in range(grid_dim+2)])))
            curr_x += 1
        # Step 3
        if direction == 0:
            curr_x -= 1
        elif direction == 1:
            curr_y += 1
        elif direction == 2:
            curr_x += 1
        else:
            curr_y -= 1
        virus_pos = [curr_x, curr_y]
        return current_grid, virus_pos, direction, counter

    def read_input(self, s):
        """
        On crée une grid. Une list de list (une deque de deque)
        """
        grid = deque()
        for str_row in s.split("\n"):
            grid.append(deque(list(map(int,str_row.replace('.','0').replace('#','2')))))
        return grid
