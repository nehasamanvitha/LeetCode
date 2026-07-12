class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        grid = [['.' for _ in range(n)] for _ in range(m)]

        def count_paths():
            dp = [[0] * n for _ in range(m)]
            if grid[0][0] == '#' or grid[m - 1][n - 1] == '#':
                return 0

            dp[0][0] = 1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '#':
                        dp[i][j] = 0
                        continue
                    if i:
                        dp[i][j] += dp[i - 1][j]
                    if j:
                        dp[i][j] += dp[i][j - 1]
                    if dp[i][j] > k:
                        dp[i][j] = k + 1
            return dp[m - 1][n - 1]

        cells = []
        for i in range(m):
            for j in range(n):
                if (i, j) != (0, 0) and (i, j) != (m - 1, n - 1):
                    cells.append((i, j))

        def dfs(idx):
            paths = count_paths()
            if paths == k:
                return True
            if paths < k or idx == len(cells):
                return False

            i, j = cells[idx]

            grid[i][j] = '#'
            if dfs(idx + 1):
                return True

            grid[i][j] = '.'
            return dfs(idx + 1)

        if dfs(0):
            return ["".join(row) for row in grid]
        return []