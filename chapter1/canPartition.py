# -*-coding: utf-8 -*-
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        W = sum(nums)/2

        N = len(nums)
        dp = [[False for i in range(W + 1)] for j in range(N + 1)]
        # dp[i][j]=true/false,选择前i个物品可以凑成重量是j的可能,true为可以,false为不行
        for i in range(N + 1):
            dp[i][0] = True
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if w - nums[i-1] < 0:
                    dp[i][w] = dp[i-1][w]
                else:
                    dp[i][w] = dp[i-1][w-nums[i-1]] | dp[i-1][w]
        return dp[N][W]
    def canPartition1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        W = sum(nums)/2

        N = len(nums)
        dp = [False for i in range(W + 1)]
        dp[0] = True
        for i in range(N):
            for j in range(W, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j-nums[i]] or dp[j]
        return dp[W]

if __name__ == "__main__":
    nums = [1,5,11,5,4]
    print Solution().canPartition1(nums)