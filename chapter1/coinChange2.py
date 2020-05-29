# -*-coding: utf-8 -*-
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 状态，j总金额，i表示coins中前i个硬币面值
        # dp[i][j]=n表示使用coins中前i个硬币面值凑成金额为j的方法有n种
        W = amount
        N = len(coins)
        dp = [[0 for i in range(W + 1)] for j in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = 1
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if w - coins[i - 1] < 0:
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = dp[i][w - coins[i-1]] + dp[i-1][w]
        return dp[N][W]
    def change2(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 状态，j总金额，i表示coins中前i个硬币面值
        # dp[i][j]=n表示使用coins中前i个硬币面值凑成金额为j的方法有n种
        W = amount
        N = len(coins)
        dp = [0 for i in range(W + 1)]
        dp[0] = 1

        for i in range(N):
            for j in range(1, W+1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i]]

        return dp[amount]
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 5
    print Solution().change(amount, coins)