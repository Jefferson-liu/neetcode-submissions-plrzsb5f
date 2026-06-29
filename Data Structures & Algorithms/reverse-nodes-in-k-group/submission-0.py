# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseK(head, k):
            cur = head
            for _ in range(k):
                if cur is None:
                    return (head, None)        # fewer than k nodes: leave intact
                cur = cur.next
            p = cur                    # (k+1)th node — tail links here, into the remainder
            cur = head
            for _ in range(k):
                temp = cur.next
                cur.next = p
                p = cur
                cur = temp
            return (p,head)
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            newHead, newTail = reverseK(groupPrev.next, k)
            if newTail is None:              # leftover < k, leave intact and stop
                break
            groupPrev.next = newHead         # connect prev tail -> this group's new head
            groupPrev = newTail              # this group's tail is the next prev
        return dummy.next