class RandomizedSet:

    def __init__(self):
        self.val_set = dict()

    def insert(self, val: int) -> bool:
        if self.val_set.get(val, 0) == 0:
            self.val_set[val] = 1
            return True

        return False

    def remove(self, val: int) -> bool:
        if self.val_set.get(val, 0) != 0:
            del self.val_set[val]
            return True
        
        return False
        
    def getRandom(self) -> int:

        return random.choice(list(self.val_set.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
