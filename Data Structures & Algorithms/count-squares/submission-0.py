class CountSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))
        

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1    
        

    def count(self, point: List[int]) -> int:
        combs = 0
        x1, y1 = point
        for y2 in self.points[x1]:
            length = y2 - y1
            if length == 0:
                continue
            
            x3, x4 = x1 + length, x1 - length
            combs += self.points[x1][y2] * self.points[x3][y1] * self.points[x3][y2]
            combs += self.points[x1][y2] * self.points[x4][y1] * self.points[x4][y2]
        return combs