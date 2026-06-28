"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head
        nodeMap = {}
        refMap = {}
        seen = set()
        counter = 0
        while cur:
            if cur not in seen:
                nodeMap[counter] = Node(cur.val, None, None)
                refMap[cur] = counter
                counter += 1
                
            cur = cur.next
        
        randMap = {}
        # counter, each index is a random one
        cur = head
        while cur:
            if cur.random:
                randMap[refMap[cur]] = refMap[cur.random]
            else:
                randMap[refMap[cur]] = None
            cur = cur.next
        # next vals
        for i in range(counter):
            if i + 1 < counter:
                nodeMap[i].next = nodeMap[i + 1]
            if randMap[i] is not None:
                nodeMap[i].random = nodeMap[randMap[i]]
            else:
                nodeMap[i].random = None
        if 0 in nodeMap:
            return nodeMap[0]
        return None
        
