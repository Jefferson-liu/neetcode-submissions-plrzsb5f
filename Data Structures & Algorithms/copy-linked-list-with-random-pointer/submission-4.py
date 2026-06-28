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
        
        nodeMap = {}

        cur = head
        while cur:
            if cur not in nodeMap:
                nodeMap[cur] = Node(0)

            nodeMap[cur].val = cur.val
            if cur.next in nodeMap:
                nodeMap[cur].next = nodeMap[cur.next]
            else:
                if cur.next is not None:
                    nodeMap[cur.next] = Node(cur.next.val)
                    nodeMap[cur].next = nodeMap[cur.next]
            
            if cur.random in nodeMap:
                nodeMap[cur].random = nodeMap[cur.random]
            else:
                if cur.random is None:
                    nodeMap[cur].random = None
                else:
                    nodeMap[cur.random] = Node(cur.random.val)
                    nodeMap[cur].random = nodeMap[cur.random]
            cur = cur.next
        if head:
            return nodeMap[head]
        return None
            
        
