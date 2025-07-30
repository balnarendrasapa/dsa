"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return None

        curr = head
        o_t_n = {}
        while curr:
            o_t_n[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clone = o_t_n[curr]
            clone.next = o_t_n.get(curr.next)
            clone.random = o_t_n.get(curr.random)
            curr = curr.next

        return o_t_n[head]
