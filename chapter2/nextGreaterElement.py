class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = []
        ans = {}
        ansl = []
        n = len(nums1)
        m = len(nums2)
        for i in range(m-1, -1, -1):
            while s and s[-1] <= nums2[i]:
                s.pop()
            ans[nums2[i]] = -1 if not s else s[-1]
            s.append(nums2[i])
        for i in nums1:
            ansl.append(ans[i])
        return ansl

if __name__ == "__main__":
    print Solution().nextGreaterElements([1,2,1])