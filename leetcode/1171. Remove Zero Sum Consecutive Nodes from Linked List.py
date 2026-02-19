# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix = 0
        seen = {}
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr:
            prefix += curr.val
            seen[prefix] = curr
            curr = curr.next

        prefix = 0
        curr = dummy
        while curr:
            prefix += curr.val
            curr.next = seen[prefix].next
            curr = curr.next

        return dummy.next
