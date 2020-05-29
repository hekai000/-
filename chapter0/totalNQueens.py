# -*- coding: utf-8 -*-
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
#  上图为 8 皇后问题的一种解法。
#
#  给定一个整数 n，返回 n 皇后不同的解决方案的数量。
#
#  示例:
#
#  输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#
#
#
#
#  提示：
#
#
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步
# ，可进可退。（引用自 百度百科 - 皇后 ）
#
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValid(self, path, row, col):
        # 同一列有无Q
        for i in range(len(path)):
            if path[i][col] == 'Q': return False
        i = row - 1
        j = col + 1
        while(i >= 0 and j < len(path)):
            if path[i][j] == 'Q': return False
            i -= 1
            j += 1
        i = row - 1
        j = col - 1
        while(i >= 0 and j >= 0):
            if path[i][j] == 'Q': return False
            i -= 1
            j -= 1
        return True
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        from copy import deepcopy
        result = []
        board = ['.' * n for j in range(n)]

        def backtrack(path, row):
            if row == len(path):
                result.append(deepcopy(path))
                return
            col_size = len(path[0])
            for col in range(col_size):
                if not self.isValid(path, row, col):
                    continue
                path[row] = path[row][:col] + 'Q' + path[row][col + 1:]
                backtrack(path, row + 1)
                path[row] = path[row][:col] + '.' + path[row][col + 1:]

        backtrack(board, 0)
        return len(result)
# leetcode submit region end(Prohibit modification and deletion)
