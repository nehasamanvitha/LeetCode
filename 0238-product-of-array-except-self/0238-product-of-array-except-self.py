class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        left_pro=1
        for i in range(n):
            res[i]=left_pro
            left_pro*=nums[i]
        right_pro=1
        for i in range(n-1,-1,-1):
            res[i]*=right_pro
            right_pro*=nums[i]
        return res

        