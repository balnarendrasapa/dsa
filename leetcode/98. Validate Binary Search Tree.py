def validate(root, low=float('-inf'), high=float('inf')):
    if root is None:
        return True

    if not (low < root.val < high):
        return False

    return validate(root.left, low, root.val) and validate(root.right, root.val, high)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return validate(root)
