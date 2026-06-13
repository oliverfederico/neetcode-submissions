class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.prev_total = matrix
        total = 0
        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                total += self.prev_total[r][c]
                self.prev_total[r][c] = total
                self.prev_total[r][c] += self.prev_total[r][c-1] if c > 0 else 0
            total = 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prev_total[row2][col2]
        l = self.prev_total[row2][col1-1] if col1 > 0 else 0
        r = self.prev_total[row1-1][col2] if row1 > 0 else 0
        lr = self.prev_total[row1-1][col1-1] if row1 > 0 and col1 >0 else 0
        return ((total - l) - r) + lr
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)