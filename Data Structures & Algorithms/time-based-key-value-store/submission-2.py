class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((value, timestamp))
        else:
            self.store[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            vals = self.store[key]
            l = 0
            r = len(vals) - 1
            while l <= r:
                m = (l + r)//2
                if vals[m][1] == timestamp:
                    return vals[m][0]
                if vals[m][1] > timestamp:
                    r = m - 1
                else:
                    l = m + 1 
            if vals[r][1] <= timestamp:
                return vals[r][0]
        return ""
        