# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head

        even_start = head
        odd_start = head.next
        odd_head = odd_start

        while odd_start and odd_start.next:
            even_start.next = odd_start.next
            even_start = even_start.next

            odd_start.next = even_start.next
            odd_start = odd_start.next

        even_start.next = odd_head

        return head
