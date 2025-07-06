# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        temp = root
        st = deque([temp])
        result = []
        while len(st) != 0:
            level = []
            for i in range(len(st)):
                temp = st.popleft()
                level.append(temp.val)
                if temp.left:
                    st.append(temp.left)

                if temp.right:
                    st.append(temp.right)
            
            result.append(level)

        return result
