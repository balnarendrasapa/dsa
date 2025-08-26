class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        index = min(range(len(arr)), key = lambda i: abs(arr[i] - x))
        left = index - 1
        right = index + 1
        result = [arr[index]]
        k -= 1
        while left >= 0 and right < len(arr) and k > 0:
            if abs(arr[left] - x) < abs(arr[right] - x):
                result.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right]:
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
            
            k -= 1

        while k > 0 and left >= 0:
            result.append(arr[left])
            left -= 1
            k -= 1
        
        while k > 0 and right < len(arr):
            result.append(arr[right])
            right += 1
            k -= 1

        result.sort()
        return result
