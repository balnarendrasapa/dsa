# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def getTree(self, head)
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(val=head.val)

        parent = None
        slow = head
        fast = head

        while fast and fast.next:
            parent = slow
            slow = slow.next
            fast = fast.next.next

        root = TreeNode(val = slow.val)
        parent.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        slow.next = None
        
        return root
        
