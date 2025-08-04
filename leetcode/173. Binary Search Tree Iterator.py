# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class BSTIterator:

#     def __init__(self, root: Optional[TreeNode]):
#         self.stack = []
#         self.pushAll(root)

#     def pushAll(self, root):
#         while root:
#             self.stack.append(root)
#             root = root.left

#     def next(self) -> int:
#         t = self.stack.pop()
#         self.pushAll(t.right)
#         return t.val

#     def hasNext(self) -> bool:
#         return len(self.stack) > 0
        
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.root = root
        self.index = -1
        self.inorder(root)

    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        if root:
            self.arr.append(root.val)
        self.inorder(root.right)

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.arr) - 1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
