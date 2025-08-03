from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
        self.length = 0

    def get(self, key: int) -> int:
        rv = self.cache.get(key, -1)
        if rv != -1:
            self.cache.move_to_end(key)
        return rv

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if self.length == self.capacity:
                self.cache.popitem(last=False)
                self.length -= 1

            self.cache[key] = value
            self.length += 1



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
