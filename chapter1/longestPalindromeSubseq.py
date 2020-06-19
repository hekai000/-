class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            dp[i][i] = 1
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][length-1]

if __name__ == "__main__":
    s = "bbbab"
    print Solution().longestPalindromeSubseq(s)