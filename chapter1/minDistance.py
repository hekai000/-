# -*-coding: utf-8 -*-
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def dp(i, j):
            if i == -1: return j + 1
            if j == -1: return i + 1
            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(dp(i-1, j) + 1,
                           dp(i-1, j-1) + 1,
                           dp(i, j-1) + 1)
        return dp(len(word1) - 1, len(word2) - 1)
    # memo优化
    def minDistance2(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = {}
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1)
            else:
                memo[(i, j)] = min(dp(i-1, j) + 1,
                           dp(i-1, j-1) + 1,
                           dp(i, j-1) + 1)
            return memo[(i, j)]
        return dp(len(word1) - 1, len(word2) - 1)
    # dp table， 动态规划51
    def minDistance3(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        for i in range(l1 + 1):
            dp[i][0] = i
        for j in range(l2 + 1):
            dp[0][j] = j
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1,
                                   dp[i][j-1] + 1,
                                   dp[i-1][j-1] + 1)
        return dp[l1][l2]
if __name__ == "__main__":
    print Solution().minDistance("hea", "kka")