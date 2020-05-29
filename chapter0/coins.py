# -*- coding:utf-8 -*-
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回
#  -1。
#
#
#
#  示例 1:
#
#  输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
#  示例 2:
#
#  输入: coins = [2], amount = 3
# 输出: -1
#
#
#
#  说明:
# 你可以认为每种硬币的数量是无限的。
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    result = []
    path = []
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        def dp(n):
            if n == 0: return 0
            if n < 0: return -1
            res = float("inf")
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1: continue
                res = min(res, subproblem + 1)
            return res if res != float("inf") else -1
        return dp(amount)

class Solution2(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != amount+1 else -1
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    print Solution().coinChange([1,2,3,5], 6)