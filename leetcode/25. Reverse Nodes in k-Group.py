# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseNodes(head):

    prev = None

    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    
    return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        temp1 = head
        temp2 = head
        tk = 0
        p = []
        parent = None
        while temp2:
            tk += 1
            if tk == k:
                temp = temp2.next
                temp2.next = None
                temp1 = reverseNodes(temp1)

                if parent:
                    parent.next = temp1

                p.append(temp1)
                while temp1.next:
                    temp1 = temp1.next
                
                temp1.next = temp
                parent = temp1
                temp1 = temp1.next
                temp2 = temp1
                tk = 0
            else:
                temp2 = temp2.next
                
        return p[0]

        
