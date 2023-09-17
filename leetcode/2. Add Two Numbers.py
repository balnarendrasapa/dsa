# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def answer(l1, l2, carry, node):

    if l1 == None and l2 == None and carry == 0:
        return node

    if l1 == None:
        l1 = ListNode()

    if l2 == None:
        l2 = ListNode()

    sum_val = l1.val + l2.val + carry
    if sum_val < 10:
        node = ListNode(val = sum_val)
        node.next = answer(l1.next, l2.next, 0, node.next)

    elif sum_val >= 10:
        for_carry = sum_val // 10
        last_digit = sum_val % 10
        node = ListNode(val = last_digit)
        node.next = answer(l1.next, l2.next, for_carry, node.next)

    return node

    


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        return answer(l1, l2, 0, node)
        
