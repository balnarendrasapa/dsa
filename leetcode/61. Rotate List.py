# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getLength(head):
    length = 0

    while head:
        length += 1
        head = head.next

    return length

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
            
        if k == 0:
            return head

        l = getLength(head)

        if l == 1:
            return head

        k = k % l

        if k == 0:
            return head

        t = 1
        head2 = head
        while t != l - k:
            t += 1
            head2 = head2.next

        temp = head2.next
        head2.next = None
        res = temp

        while temp.next:
            temp = temp.next
        
        temp.next = head
        return res
