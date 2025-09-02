class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        lb = max(ax1, bx1)
        rb = min(ax2, bx2)

        bb = max(ay1, by1)
        tb = min(ay2, by2)

        area_1 = (ax2 - ax1) * (ay2 - ay1)
        area_2 = (bx2 - bx1) * (by2 - by1)

        if lb < rb and bb < tb:
            intersection = (rb - lb) * (tb - bb)
        else:
            intersection = 0

        return area_1 + area_2 - intersection
