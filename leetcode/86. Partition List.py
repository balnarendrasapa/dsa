# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
            
        temp = head
        parent = ListNode(0)
        parent.next = head
        second_half = ListNode(0)
        flag = False

        while temp:
            if temp.val >= x:
                if temp == head:
                    flag = True
                    head = parent
                nex = temp.next
                z = second_half
                while z.next:
                    z = z.next

                z.next = temp
                parent.next = parent.next.next
                temp.next = None
                temp = nex
            else:
                parent = temp
                temp = temp.next


        k = head
        while k.next:
            k = k.next
        
        k.next = second_half.next

        if flag:
            return head.next

        return head
