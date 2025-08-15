import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.in_heap = set()
        self.counter = 1

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.in_heap.remove(smallest)
            return smallest
        else:
            temp = self.counter
            self.counter += 1
            return temp
        

    def addBack(self, num: int) -> None:
        if num < self.counter and num not in self.in_heap:
            heapq.heappush(self.heap, num)
            self.in_heap.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
