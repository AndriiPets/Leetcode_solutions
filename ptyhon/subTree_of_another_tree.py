# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, q: TreeNode, p: TreeNode) -> bool:
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
