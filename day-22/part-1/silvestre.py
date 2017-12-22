from collections import deque
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        current_grid = self.read_input(s)

        virus_pos = [len(current_grid)//2 for i in range(2)]

        burst = 0
        counter = 0
        direction = 0
        while burst < 10000:
            current_grid, virus_pos, direction, counter = self.execute_burst(current_grid, virus_pos, direction, counter)
            burst += 1
            assert 0 <= virus_pos[0] < len(current_grid) and 0 <= virus_pos[1] < len(current_grid)
        
        return counter

    def execute_burst(self, current_grid, virus_pos, direction, counter):
        """
        Direction :
        0 - ascending
        1 - right
        2 - descending
        3 - left
        """
        # Step 1 & 2
        curr_x = virus_pos[0]
        curr_y = virus_pos[1]
        if current_grid[curr_x][curr_y] == '#':
            direction = (direction + 1) % 4
            current_grid[curr_x][curr_y] = '.'
        else:
            direction = (direction -1) % 4
            current_grid[curr_x][curr_y] = '#'
            counter += 1
        # Avant d'avancer il faut agrandir la grille si besoin
        grid_dim = len(current_grid)
        if curr_x in [0, grid_dim-1] or curr_y in [0, grid_dim-1]:
            for i in range(grid_dim):
                current_grid[i].appendleft('.')
                current_grid[i].append('.')
            curr_y += 1
            # import pdb; pdb.set_trace()
            current_grid.appendleft(deque(list(['.' for i in range(grid_dim+2)])))
            current_grid.append(deque(list(['.' for i in range(grid_dim+2)])))
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
            grid.append(deque(list(str_row)))
        return grid
