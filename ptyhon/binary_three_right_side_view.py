class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def rightSideView(self, root: TreeNode):
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            qlen = len(q)
            level = []

            for i in range(qlen):
                node = q.popleft()
                level.append(node.val)

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            res.append(level[0])
        return res
