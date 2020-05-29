# -*-coding: utf-8 -*-
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] = n, i为第i个数，n为最大和，dp[i] = n表示以第i个数结尾时，最大和为n
        dp = [nums[i] for i in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)
if __name__ == "__main__":
    print Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])