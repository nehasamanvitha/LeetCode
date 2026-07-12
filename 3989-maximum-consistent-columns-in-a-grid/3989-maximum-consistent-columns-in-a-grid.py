from typing import List

class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m, n = len(grid), len(grid[0])

        dp = [1] * n

        for j in range(n):
            for i in range(j):
                valid = True
                for r in range(m):
                    if abs(grid[r][j] - grid[r][i]) > limit:
                        valid = False
                        break
                if valid:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)
        