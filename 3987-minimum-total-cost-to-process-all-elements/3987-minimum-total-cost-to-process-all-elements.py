class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        resources = k
        operations = 0
        cost = 0

        for num in nums:
            if resources < num:
                need = num - resources
                add = (need + k - 1) // k

                cost = (cost + (operations + 1 + operations + add) * add // 2) % MOD

                operations += add
                resources += add * k

            resources -= num

        return cost