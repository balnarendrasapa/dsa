class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append((timestamp, value))
        else:
            self.d[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.d.get(key, [])
        start = 0
        end = len(values) - 1
        while start <= end:
            mid = (start + end) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                start = mid + 1
            else:
                end = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
