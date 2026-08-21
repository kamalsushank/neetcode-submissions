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
        copymap = dict()
        copymap[None] = None
        curr = head
        while curr :
            naya = Node(curr.val)
            copymap[curr] = naya
            curr = curr.next
        c = copymap[head]
        curr = head
        h1 = copymap[curr]
        while curr :
            copymap[curr].next = copymap[curr.next]
            copymap[curr].random = copymap[curr.random]
            curr = curr.next
        return h1

