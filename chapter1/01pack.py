# -*-coding: utf-8 -*-
class Solution(object):
    def maxPackValue(self, N, W, wt,val):
        dp = [[0 for i in range(W+1)] for j in range(N+1)]
        for i in range(1, N+1):
            for w in range(1, W+1):
                if w - wt[i-1] < 0:
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = max(dp[i-1][w-wt[i-1]] + val[i-1], dp[i-1][w])
        return dp[N][W]

if __name__ == "__main__":
    N = 3
    W = 4
    wt = [2, 1, 3]
    val = [4, 2, 3]
    print Solution().maxPackValue(N, W, wt,val)