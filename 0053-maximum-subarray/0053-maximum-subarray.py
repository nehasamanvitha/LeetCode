class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = global_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            global_sum = max(global_sum, curr_sum)

        return global_sum




    
        