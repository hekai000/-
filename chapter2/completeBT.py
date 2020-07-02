class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import math
        if not root: return 0
        l, r = root, root
        hl, hr = 0, 0
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        if hl == hr:
            return math.pow(2, hl) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def main():
    import sys

    try:
        line = "[1,2,3,4,5,6]"
        root = stringToTreeNode(line)

        ret = Solution().countNodes(root)

        out = intToString(ret)
        print out
    except StopIteration:
        pass


if __name__ == '__main__':
    main()