def getNewRow(arr):
    temp = [0 for _ in range(len(arr) - 1)]
    j = 0
    for i in range(1, len(arr)):
        temp[j] = arr[i - 1] + arr[i]
        j += 1

    return temp

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        if numRows == 1:
            return result

        for _ in range(2, numRows + 1):
            last_row = [0] + result[-1] + [0]
            new_row = getNewRow(last_row)
            result.append(new_row)

        return result
