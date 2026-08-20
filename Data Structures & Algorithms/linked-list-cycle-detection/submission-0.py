# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s1 = dict()
        c = head
        index = -1
        i=0
        while c:
            if c in s1 :
                index = s1[c]
                return True
            else:
                s1[c] = i
                i+=1
            c = c.next
        return False