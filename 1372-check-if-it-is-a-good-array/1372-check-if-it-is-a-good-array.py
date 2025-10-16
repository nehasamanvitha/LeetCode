class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        from math import gcd
        from functools import reduce
        return reduce(gcd,nums)==1
        