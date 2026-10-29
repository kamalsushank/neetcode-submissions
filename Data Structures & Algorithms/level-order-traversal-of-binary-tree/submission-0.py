# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue = deque()
        res = []
        queue.append([root])
        while queue :
            tmp = []
            nodes = queue.popleft()
            res.append([node.val for node in nodes])
            for i in nodes :
                if i.left :
                    tmp.append(i.left)
                if i.right :
                    tmp.append(i.right)
            if tmp :
                queue.append(tmp)
        return res