class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        mn = val if not self.st else min(self.st[-1][1], val)
        self.st.append((val, mn))

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
        
