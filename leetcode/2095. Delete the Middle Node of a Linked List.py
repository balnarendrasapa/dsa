# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        slow = head
        fast = head
        parent = None

        while fast and fast.next:
            parent = slow
            slow = slow.next
            fast = fast.next.next

        parent.next = parent.next.next

        return head
