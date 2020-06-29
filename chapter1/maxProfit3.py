class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n)]
        for i in range(n):
            for k in range(2, -1, -1):
                if i == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[0]
                    continue

                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[n-1][2][0]

if __name__ == "__main__":
    print Solution().maxProfit([1,2,3,4,5])