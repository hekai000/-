class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    memo = {}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root in self.memo:
            return self.memo[root]
        if root.left:
            w_left = self.rob(root.left.left) + self.rob(root.left.right)
        else:
            w_left = 0

        if root.right:
            w_right = self.rob(root.right.left) + self.rob(root.right.right)
        else:
            w_right = 0

        do_it = root.val + w_left + w_right
        not_do = self.rob(root.left) + self.rob(root.right)
        res = max(do_it, not_do)
        self.memo[root] = res
        return res

if __name__ == "__main__":
    root = TreeNode(3)
    v2 = TreeNode(2)
    v3 = TreeNode(3)
    v4 = TreeNode(3)
    v5 = TreeNode(1)
    root.left = v2
    root.right = v3
    v2.left = None
    v2.right = v4
    v3.left = None
    v3.right = v5
    print Solution().rob(root)