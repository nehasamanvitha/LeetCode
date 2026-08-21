class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])

        row_sum = [sum(row) for row in grid]
        col_sum = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        total = sum(row_sum)

        # Horizontal cut
        curr = 0
        for i in range(m - 1):
            curr += row_sum[i]
            if curr * 2 == total:
                return True

        # Vertical cut
        curr = 0
        for j in range(n - 1):
            curr += col_sum[j]
            if curr * 2 == total:
                return True

        return False