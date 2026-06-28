# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenList = 0
        cur = head
        while cur:
            cur = cur.next
            lenList += 1
        
        cur = head
        prev = None
        count = 0
        while cur and count < (lenList - n):
            prev = cur
            cur = cur.next
            count += 1
        
        if prev:
            prev.next = cur.next
        else:
            return head.next

        return head