class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        dp_i_1 = 0
        dp_i_2 = 0
        dp_i = 0
        for i in range(n-1, -1, -1):
            dp_i = max(dp_i_1, dp_i_2 + nums[i])
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i
if __name__ == "__main__":
    print Solution().rob([1,2,3,5])