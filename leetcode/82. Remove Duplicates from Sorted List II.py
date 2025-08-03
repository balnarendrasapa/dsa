# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        stack = {}
        while temp and temp.next:
            if temp.val == temp.next.val:
                stack[temp.val] = 1
            temp = temp.next

        stack = list(stack.keys())

        temp = head
        newHead = ListNode(0)
        result = newHead
        while temp:
            if temp.val not in stack:
                node = ListNode(temp.val)
                newHead.next = node
                newHead = newHead.next
            
            temp = temp.next

        return result.next
