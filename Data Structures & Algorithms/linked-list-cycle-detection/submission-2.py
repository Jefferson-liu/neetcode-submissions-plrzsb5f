# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast pointer and slow pointer
        fast = head
        slow = head

        while fast and slow and fast.next:
            #print(fast.val)
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False