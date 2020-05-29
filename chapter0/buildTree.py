class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    pre_idx = 0
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
# leetcode submit region end(Prohibit modification and deletion)
        def helper(in_left=0, in_right=len(inorder)):
            if in_left == in_right:
                return None
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            index = idx_map[root_val]
            self.pre_idx += 1
            root.left = helper(in_left, index)
            root.right = helper(index+1, in_right)
            return root
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return helper()
if __name__ == "__main__":
    r = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
    print(r)