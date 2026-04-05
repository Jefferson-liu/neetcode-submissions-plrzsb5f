# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # we will have two nodes we are looking at/pointers, let n1 = node at list1 and n2 = node at l2
        # if n1.val < n2.val, result.add n1.val, n1 = n1.next, else result.add n2.val
        ans = ListNode()
        n1 = list1
        n2 = list2
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if n1.val < n2.val:
            ans = n1
            n1 = n1.next
        else:
            ans = n2
            n2 = n2.next
        while n1 is not None or n2 is not None:
            if n1 and n2:
                if n1.val < n2.val:
                    ans.next = n1
                    n1 = n1.next
                    ans = ans.next
                else:
                    ans.next = n2
                    n2 = n2.next
                    ans = ans.next
            elif n1:
                ans.next = n1
                n1 = n1.next
                ans = ans.next
            else:
                ans.next = n2
                n2 = n2.next
                ans = ans.next

        if list1.val < list2.val:
            return list1
        else:
            return list2

            