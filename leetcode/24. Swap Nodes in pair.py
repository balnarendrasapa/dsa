# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        res = head
        while head != None and head.next != None:
            temp = head.val
            temp_next = head.next.val
            head.val = temp_next
            head.next.val = temp
            head = head.next.next

        return res
        
