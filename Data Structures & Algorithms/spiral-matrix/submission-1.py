class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        while matrix:
            spiral.extend(matrix.pop(0))

            if matrix and matrix[0]:
                for r in matrix:
                    spiral.append(r.pop())
            
            if matrix:
                spiral.extend(matrix.pop()[::-1])
            
            if matrix and matrix[0]:
                for r in matrix[::-1]:
                    spiral.append(r.pop(0))
        return spiral
