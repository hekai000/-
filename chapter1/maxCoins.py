# class Solution(object):
#     result = float("-INF")
#     def maxCoins(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#
#         def backtrack(nums, scores):
#             if not nums:
#                 self.result = max(self.result, scores)
#                 return
#
#             for i in range(len(nums)):
#                 if i - 1 < 0 and i + 1 >= len(nums):
#                     point = nums[i]
#                 elif i - 1 < 0:
#                     point = nums[i]*nums[i+1]
#                 elif i + 1 >= len(nums):
#                     point = nums[i-1] * nums[i]
#                 else:
#                     point = nums[i-1]*nums[i]*nums[i+1]
#
#                 nums1 = nums[:i] + nums[i+1:]
#                 backtrack(nums1, scores + point)
#
#
#         backtrack(nums, 0)
#         return self.result
class Solution(object):

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums1 = [1] + nums + [1]
        dp = [[0 for i in range(len(nums1))] for j in range(len(nums1))]
        for i in range(len(nums1) - 2, -1, -1):
            for j in range(i + 1, len(nums1)):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums1[i]*nums1[k]*nums1[j])
        return dp[0][len(nums)+1]
if __name__ == "__main__":
    print Solution().maxCoins([3,1,5,8])
