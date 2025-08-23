# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode()

        curr = head

        while curr:
            nxt = curr.next

            prev = result

            while prev.next and prev.next.val < curr.val:
                prev = prev.next


            curr.next = prev.next
            prev.next = curr

            curr = nxt

        return result.next

