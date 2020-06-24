class Solution(object):
    def kmp(self, needle):
        n = len(needle)
        dp = [[0 for _ in range(256)] for _ in range(n)]
        dp[0][ord(needle[0])] = 1
        X = 0
        for j in range(1, n):
            for c in range(256):
                dp[j][c] = dp[X][c]
            dp[j][ord(needle[j])] = j + 1
            X = dp[X][ord(needle[j])]
        return dp

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        j = 0
        dp = self.kmp(needle)
        for i in range(n):
            j = dp[j][ord(haystack[i])]
            if j == m:
                return i - m + 1
        return -1

if __name__ == "__main__":
    haystack = "cabaababac"
    needle = "ababa"
    print Solution().strStr(haystack, needle)