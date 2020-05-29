class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    res = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(node):

            if not node: return 0
            max_left = max(0, traverse(node.left))
            max_right = max(0, traverse(node.right))
            self.res = max(self.res, node.val + max_left + max_right)
            return node.val + max(max_left, max_right)


        traverse(root)
        return self.res

if __name__ == "__main__":
    a = TreeNode(-51)
    b = TreeNode(2)
    c = TreeNode(3)
    a.left = b
    a.right = c
    print Solution().maxPathSum(a)