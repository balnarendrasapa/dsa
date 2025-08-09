# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = []
        B = []

        temp = headA
        while temp:
            A.append(temp)
            temp = temp.next

        temp = headB
        while temp:
            B.append(temp)
            temp = temp.next

        
        i = len(A) - 1
        j = len(B) - 1

        while i >= 0 and j >= 0 and A[i] == B[j]:
            i -= 1
            j -= 1

        if i == len(A) - 1:
            return None
            
        return A[i + 1]
