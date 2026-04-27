class Node:
    def __init__(self, key, value, prev=None, nxt=None) -> None:
        self.key = key
        self.value = value
        self.prev = prev
        self.nxt = nxt

class LRUCache:
    # constant access, constant delete throughout, constant add front. Queue + hashmap?
    # Queue is linked list of key and value? keys map to value + linked list of keys?
    # HM key = lru key, value = ll object | ll object has lru value + key as we need to get from ll to map
    def __init__(self, capacity: int):
        self.kv_map = {}
        self.head = None
        self.cap = capacity
        self.tail = None
    
    # map lookup + ll move to front
    def get(self, key: int) -> int:
        if key in self.kv_map:
            found = self.kv_map[key]
            if found != self.tail:
                if found == self.head:
                    self.head = found.nxt
                    self.head.prev = None
                else:
                    found.prev.nxt = found.nxt
                    found.nxt.prev = found.prev

                found.nxt = None
                found.prev = self.tail
                self.tail.nxt = found
                self.tail = found
            return found.value
        else:
            return -1
        
        
    # map lookup, if not in then add to ll and map
    # if full then remove last value in ll 
    # if exist then update key and ll move to front
    def put(self, key: int, value: int) -> None:
        if key in self.kv_map:
            found = self.kv_map[key]
            found.value = value
            # Same as get
            if found != self.tail:
                if found == self.head:
                    self.head = found.nxt
                    self.head.prev = None
                else:
                    found.prev.nxt = found.nxt
                    found.nxt.prev = found.prev

                found.nxt = None
                found.prev = self.tail
                self.tail.nxt = found
                self.tail = found
        else:
            # tail is new kv
            self.kv_map[key] = Node(key, value, prev=self.tail)
            if self.tail:
                self.tail.nxt = self.kv_map[key]
            self.tail = self.kv_map[key]
            if not self.head:
                self.head = self.kv_map[key]
            if len(self.kv_map) > self.cap:
                #pop lru, head
                self.kv_map.pop(self.head.key)
                self.head = self.head.nxt
                self.head.prev = None


