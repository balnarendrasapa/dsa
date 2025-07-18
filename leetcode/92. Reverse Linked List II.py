# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        curr = 1

        temp1 = head
        r1 = None
        while curr != left:
            r1 = temp1
            temp1 = temp1.next
            curr += 1

        if r1:
            r1.next = None

        temp2 = temp1
        while curr != right:
            temp2 = temp2.next
            curr += 1

        r2 = None
        if temp2:
            r2 = temp2.next
            temp2.next = None

        prev = None
        while temp1:
            j = temp1.next
            temp1.next = prev
            prev = temp1
            temp1 = j

        if r1:
            r1.next = prev
        else:
            head = prev

        while prev.next:
            prev = prev.next

        if r2:
            prev.next = r2

        return head
