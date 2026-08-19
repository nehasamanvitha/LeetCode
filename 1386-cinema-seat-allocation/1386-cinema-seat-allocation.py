class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        rows = {}

        for r, c in reservedSeats:
            rows.setdefault(r, set()).add(c)

        ans = (n - len(rows)) * 2

        for seats in rows.values():
            left = all(c not in seats for c in range(2, 6))
            right = all(c not in seats for c in range(6, 10))
            middle = all(c not in seats for c in range(4, 8))

            if left and right:
                ans += 2
            elif left or right or middle:
                ans += 1

        return ans
        