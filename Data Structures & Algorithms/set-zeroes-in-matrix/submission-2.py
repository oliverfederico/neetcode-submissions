class Solution:
    # we could iterate over m, find a zero, set zero for the rest of that row and 
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowZero = False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    if r == 0:
                        rowZero = True
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0 
        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0
        if rowZero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        