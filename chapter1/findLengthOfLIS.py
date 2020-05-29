class Solution(object):
    def findLengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0

        length = len(nums)
        dp = [1 for i in range(length)]

        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(res, max(dp))
    def findLengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        piles = 0
        top = {}
        for i in range(len(nums)):
            left = 0
            right = piles - 1
            poker = nums[i]
            while left <= right:
                mid = left + (right - left)/2
                if  top[mid] > poker:
                    right = mid - 1
                elif top[mid] < poker:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == piles: piles += 1
            top[left] = poker
        return piles
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        window = []

        left = 0
        right = 0
        res = 0
        while right < len(nums):
            c = nums[right]

            if window and c > window[-1]:
                window.append(c)
            elif not window:
                window.append(c)
            else:
                res = max(res, right - left)
                window = [c]

                left = right
            right += 1
        return max(res, right - left)



if __name__ == "__main__":
    #print Solution().findLengthOfLIS2([1,4,3,4,2])
    print Solution().findLengthOfLCIS([1,3,5,4,2,3,4,5])