# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = [l for l in lists]
        minVal = math.inf
        minInd = -1
        for i, l in enumerate(temp):
            if l.val < minVal:
                minVal = l.val
                minInd = i
        if minInd == -1:
                return 
        head = temp[minInd]
        temp[minInd] = temp[minInd].next
        curNode = head

        while any([l is not None for l in temp]):
            minVal = math.inf
            minInd = -1
            for i, l in enumerate(temp):
                if l:
                    if l.val < minVal:
                        minVal = l.val
                        minInd = i
            if minInd == -1:
                break
            curNode.next = temp[minInd]
            temp[minInd] = temp[minInd].next
            curNode = curNode.next
        
        return head
