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

        def copyList(node):
            if node is None:
                return None
            if node in nodeMap:
                return nodeMap[node]
            
            copy = Node(node.val)
            nodeMap[node] = copy
            copy.next = copyList(node.next)
            copy.random = nodeMap.get(node.random)
            return copy
            
        return copyList(head)
        
