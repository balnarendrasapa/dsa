from functools import cmp_to_key

class Solution:

    def getSum(num: int):
        num = str(num)
        result = 0
        for i in num:
            result += int(i)
        return result

    def minSwaps(self, nums: List[int]) -> int:
        sum_list = [[nums[i], Solution.getSum(nums[i]), i] for i in range(len(nums))]
        
        def compare(a, b):
            if a[1] > b[1]:
                return 1
            
            elif a[1] < b[1]:
                return -1
            
            else:
                if a[0] > b[0]:
                    return 1
                elif a[0] < b[0]:
                    return -1
                else:
                    return 0


        sum_list.sort(key=cmp_to_key(compare))
        print(sum_list)
        n = len(sum_list)
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or sum_list[i][2] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = sum_list[j][2]
                cycle_size += 1

            # print(cycle_size)
            if cycle_size > 1:
                swaps += (cycle_size - 1)

        return swaps
