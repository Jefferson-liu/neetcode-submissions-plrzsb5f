# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # reorder the list such that its 0, n-1, 1, n-2 etcetc
        # what is the insight
        # we can alternate reversing the heads
        def reverse(node):
            prev = None
            nextNode = None
            if node is None:
                return node
            else:
                # reverse the list
                while node:
                    nextNode = node.next
                    node.next = prev
                    prev = node
                    node = nextNode
                return prev
        
        cur = head
        while cur:
            cur.next = reverse(cur.next)
            cur = cur.next