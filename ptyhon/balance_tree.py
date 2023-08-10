# Time complexity is O(n2) needs improvment
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if abs(self.maxDepth(root.right) - self.maxDepth(root.left)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
