class MyHashSet:

    def __init__(self):
        self.hmap = {}
        

    def add(self, key: int) -> None:
        self.hmap[key] = True
        

    def remove(self, key: int) -> None:
        self.hmap[key] = False

    def contains(self, key: int) -> bool:
        return key in self.hmap and self.hmap[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)