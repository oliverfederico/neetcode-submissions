class MyStack:
    # two FIFO into one LIFO
    # we want one queue to always pop stack head
    # we want one queue to always 
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x: int) -> None:
        while self.q2:
            self.q1.append(self.q2.popleft())
        self.q1, self.q2 = self.q2, self.q1
        self.q1.append(x)

    def pop(self) -> int:
        res = self.q1.popleft()
        if self.q2:
            self.q1.append(self.q2.popleft())
        return res

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()