class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        preSumDict = {0: 1}
        ans = 0
        sum0_i = 0
        for i in range(len(nums)):
            sum0_i += nums[i]
            sum0_j = sum0_i - k
            if sum0_j in preSumDict:
                ans += preSumDict[sum0_j]
            preSumDict[sum0_i] = preSumDict.get(sum0_i, 0) + 1
        return ans

if __name__ == "__main__":
    nums = [1,2,1,3]
    k = 3
    Solution().subarraySum(nums, k)