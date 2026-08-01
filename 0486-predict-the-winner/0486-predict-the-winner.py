class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # One element remaining
        for i in range(n):
            dp[i][i] = nums[i]

        # Build intervals
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                left = nums[i] - dp[i + 1][j]
                right = nums[j] - dp[i][j - 1]

                dp[i][j] = max(left, right)

        return dp[0][n - 1] >= 0