# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        head = None

        if cur1 and cur2:
            if cur1.val > cur2.val:
                head = cur2
                cur2 = cur2.next
            else:
                head = cur1
                cur1 = cur1.next
        else:
            head = cur1 if cur1 else cur2
            if cur1:
                cur1 = cur1.next
            elif cur2:
                cur2 = cur2.next
            else:
                return None

        curNode = head
        
        while (cur1 or cur2) and curNode:
            if cur1 and cur2:
                if cur1.val < cur2.val:
                    curNode.next = cur1
                    cur1 = cur1.next
                else:
                    curNode.next = cur2
                    cur2 = cur2.next
            else:
                curNode.next = cur1 if cur1 else cur2
                if cur1:
                    cur1 = cur1.next  
                elif cur2:
                    cur2 = cur2.next
                
            curNode = curNode.next
                   
        return head