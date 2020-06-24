class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        dp = [[(0, 0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = (piles[i], 0)
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                left = dp[i+1][j][1] + piles[i]
                right = dp[i][j-1][1] + piles[j]
                if left > right:
                    dp[i][j] = (left, dp[i+1][j][0])
                else:
                    dp[i][j] = (right, dp[i][j-1][0])
        return True if dp[0][n-1][0] > dp[0][n-1][1] else False

if __name__ == "__main__":
    piles = [5,3,4,5]
    print Solution().stoneGame(piles)