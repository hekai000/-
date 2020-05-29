# -*- coding:utf-8 -*-
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

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        from copy import deepcopy
        result = []
        board = ['.'* n for j in range(n)]
        def backtrack(path, row):
            if row == len(path):
                result.append(deepcopy(path))
                return
            col_size = len(path[0])
            for col in range(col_size):
                if not self.isValid(path, row, col):
                    continue
                path[row] = path[row][:col] + 'Q' + path[row][col+1:]
                backtrack(path, row + 1)
                path[row] = path[row][:col] + '.' + path[row][col+1:]

        backtrack(board, 0)
        return result

if __name__ == "__main__":
    print Solution().solveNQueens(4)