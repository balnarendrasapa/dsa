# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge(root1, root2):
    dummy = ListNode()
    tail = dummy

    while root1 and root2:
        if root1.val < root2.val:
            tail.next = root1
            root1 = root1.next
        else:
            tail.next = root2
            root2 = root2.next
        tail = tail.next

    tail.next = root1 if root1 else root2

    return dummy.next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return merge(left, right)
