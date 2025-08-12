# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        array = []

        while head:
            array.append(head.val)
            head = head.next

        n = len(array)
        result = 0
        for i in range(n // 2):
            result = max(result, array[i] + array[n - i - 1])

        return result
