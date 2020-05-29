class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def backtrack(path, choices):
            if len(path) == len(nums):

                result.append(path[:])
                return
            for choice in choices:
                if choice in path: continue
                path.append(choice)
                backtrack(path, choices)
                path.pop()
        backtrack([], nums)
        return result

if __name__ == "__main__":
    print Solution().permute([1,2,3])
