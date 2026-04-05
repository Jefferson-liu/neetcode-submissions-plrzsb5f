# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # fast pointer, slow pointer
        # fast pointer goes until the end, note down the length of the list, 
        # slow pointer then goes until that list O(n) time O(1) space store only constants

        lenList = 0
        cur = head
        if not cur:
            return head
        
        while cur is not None:
            cur = cur.next
            lenList += 1
        
        cur1 = head
        num = lenList - n
        print(num)
        i = 0
        prev = None
        while cur1 is not None:
            if i == num:
                #remove
                if prev:
                    prev.next = cur1.next
                else:
                    return cur1.next
            prev = cur1
            cur1 = cur1.next
            i += 1

        return head
