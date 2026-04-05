# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split into two lists
        cur = head
        fast = head
        prev = None
        if head.next is None:
            return 
        while fast is not None and fast.next is not None:
            prev = cur
            cur = cur.next
            fast = fast.next.next
            
        prev.next = None
        top1 = head
        top2 = cur

        t1 = top1
        
        while t1 is not None:
            #print(t1.val)
            t1 = t1.next

        #reverse t2
        prev = None
        nextNode = None

        t2 = top2
        while t2.next is not None:
            nextNode = t2.next
            t2.next = prev
            prev = t2
            t2 = nextNode

        t2.next = prev
        top2 = t2
        while t2 is not None:
            #print(t2.val)
            t2 = t2.next
        
        n1 = top1
        n2 = top2

        while n1.next is not None:
            temp = n1.next
            temp2 = n2.next
            n1.next = n2
            n2.next = temp
            n2 = temp2
            n1 = temp
                
        if n2 is not None:
            n1.next = n2














