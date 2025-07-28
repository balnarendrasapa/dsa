import bisect
import math

class MedianFinder:

    def __init__(self):
        self.arr = []
        self.length = 0

    def addNum(self, num: int) -> None:
        bisect.insort(self.arr, num)
        self.length += 1

    def findMedian(self) -> float:
        left = math.ceil((self.length - 1) / 2)
        right = math.floor((self.length - 1)/ 2)
        return float((self.arr[left] + self.arr[right]) / 2)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
