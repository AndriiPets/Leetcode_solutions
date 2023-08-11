class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        res = []

        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []

            for i in range(qlen):
                nod = q.popleft()
                level.append(nod.val)

                if nod.left:
                    q.append(nod.left)
                if nod.right:
                    q.append(nod.right)
            res.append(level)

        return res
