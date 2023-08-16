class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = deque()
        stack.append([root, root.val])
        count = 0

        while stack:
            n = stack.pop()
            node, pathmax = n[0], n[1]
            if node.val >= pathmax:
                count += 1
                pathmax = node.val

            if node.left:
                stack.append([node.left, pathmax])
            if node.right:
                stack.append([node.right, pathmax])
        return count
