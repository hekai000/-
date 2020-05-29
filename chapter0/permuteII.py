class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        from collections import Counter
        dict_map = Counter(nums)
        def backtrack(path, choices):
            if len(path) == len(nums) and path not in result:
                result.append(path[:])
                return
            for choice in choices:
                if choice in path:
                    a = Counter(path)
                    if dict_map[choice] <= a[choice]:
                        continue
                path.append(choice)
                backtrack(path, choices)
                path.pop()
        backtrack([], nums)
        return result

if __name__ == "__main__":
    print Solution().permuteUnique([1,1,3])
