# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        temp_ll = res
        t = 0
        while head:
            if head.val == 0 and t != 0:
                temp_ll.next = ListNode(t)
                temp_ll = temp_ll.next
                t = 0

            t += head.val
            head = head.next

        return res.next
