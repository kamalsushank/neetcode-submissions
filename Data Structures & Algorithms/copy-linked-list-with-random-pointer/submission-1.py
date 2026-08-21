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
        # copymap = dict()
        # copymap[None] = None
        # curr = head
        # while curr :
        #     naya = Node(curr.val)
        #     copymap[curr] = naya
        #     curr = curr.next
        # c = copymap[head]
        # curr = head
        # h1 = copymap[curr]
        # while curr :
        #     copymap[curr].next = copymap[curr.next]
        #     copymap[curr].random = copymap[curr.random]
        #     curr = curr.next
        # return h1

        
        if not head:
            return None

        # Step 1: Create interleaved cloned nodes
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next

        # Step 2: Assign random pointers to the cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the cloned list from the original list
        curr = head
        copy_head = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next

        return copy_head
        