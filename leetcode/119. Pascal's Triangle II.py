def getNewRow(arr):
    temp = [0 for _ in range(len(arr) - 1)]
    j = 0
    for i in range(1, len(arr)):
        temp[j] = arr[i - 1] + arr[i]
        j += 1
    return temp

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]

        for _ in range(rowIndex):
            last_row = [0] + result + [0]
            result = getNewRow(last_row)

        return result
