class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        groups = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num == '.':
                    continue
                for group in [(i, -1), (-1, j), (i//3, j//3)]:
                    if num in groups[group]:
                        return False
                    groups[group].add(num)
        return True


        