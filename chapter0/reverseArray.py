class Solution(object):
    def reverseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

if __name__ == "__main__":
    print Solution().reverseArray([1,1,3])