# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a -> b -> c
        # store prev, store cur, store next
        # when prev is not none, 
        # prev: a, cur: b, next: c
        # a <-b c (cur.next = prev)
        # a <- b <- c (cur = cur.next) repeat 

        cur = head
        prev = None
        nextNode = None
        i = 0
        while cur is not None:
            nextNode = cur.next
            print(cur.val)
            cur.next = prev
            prev = cur
            cur = nextNode
            #print(prev.val)
            #print(cur is not None)


        return prev

            