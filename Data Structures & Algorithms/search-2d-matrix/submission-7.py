class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2 binary searchs vs 1 combined:
        low = 0
        high = len(matrix)
        while low < high:
            mid = (high + low) // 2
            if matrix[mid][0] > target:
                high = mid
            elif matrix[mid][-1] >= target:
                low = mid
                break
            else:
                low = mid + 1
                if low >= len(matrix):
                    return False

        row = low
        low = 0
        high = len(matrix[row])
        while low < high:
            mid = (high+low) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                high = mid
            else:
                low = mid + 1
        return False