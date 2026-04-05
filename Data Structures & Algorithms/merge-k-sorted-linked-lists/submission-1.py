# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for i, ls in enumerate(lists):
            heapq.heappush(heap, (ls.val, i, ls))
        
        dummy = ListNode()
        cur = dummy
        while heap:
            val, ind, node = heapq.heappop(heap)
            cur.next = node
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, ind, node))
            cur = cur.next
        
        return dummy.next
