class MyStack:
    # two FIFO into one LIFO
    # we want one queue to always pop stack head
    # we want one queue to always 
    def __init__(self):
        self.q = None


    def push(self, x: int) -> None:
        self.q = (x, self.q)

    def pop(self) -> int:
        top, self.q = self.q
        return top

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()