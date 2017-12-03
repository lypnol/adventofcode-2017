import math
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        matrix = [[5,4,2],[10,1,1],[11,23,25]]
        
        n = int(s)
        
        while matrix[-1][-1] < n :
            matrix[-1].append(matrix[-1][-1] + matrix[-2][-1])
            row_inv = 2
            while row_inv < len(matrix):
                matrix[-row_inv].append(matrix[-row_inv+1][-1] + matrix[-row_inv][-1] + matrix[-row_inv-1][-1] + matrix[-row_inv+1][-2])
                row_inv += 1
            matrix[-row_inv].append(matrix[-row_inv+1][-1] + matrix[-row_inv][-1] + matrix[-row_inv+1][-2])
            new_first_row = [matrix[0][-1] + matrix[0][-2]]
            col_inv = 2
            while col_inv < len(matrix[0]):
                new_first_row.insert(0,new_first_row[0]+matrix[0][-col_inv]+matrix[0][-col_inv+1] + matrix[0][-col_inv-1])
                col_inv += 1
            new_first_row.insert(0,new_first_row[0]+matrix[0][-col_inv]+matrix[0][-col_inv+1])
            new_first_row.insert(0,new_first_row[0]+ matrix[0][0])
            matrix.insert(0, new_first_row)
            row = 1
            while row < (len(matrix[0])-2):
                matrix[row].insert(0,matrix[row-1][0] + matrix[row-1][1] + matrix[row][0] + matrix[row+1][0])
                row += 1
            matrix[row].insert(0,matrix[row-1][0] + matrix[row-1][1] + matrix[row][0])
            new_last_row = [matrix[-1][0] + matrix[-1][1]]
            col = 1
            while col < len(matrix[0])-1:
                new_last_row.append(new_last_row[-1] + matrix[-1][col-1] + matrix[-1][col] + matrix[-1][col+1])
                col += 1
            new_last_row.append(new_last_row[-1] + matrix[-1][col-1] + matrix[-1][col])
            matrix.append(new_last_row)

        print(matrix)
        result = max(max(row) for row in matrix)
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                if matrix[i][j] >= n and matrix[i][j] < result :
                    result = matrix[i][j]
            
        return result

