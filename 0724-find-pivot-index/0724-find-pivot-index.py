class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        sum1=0
        n=len(nums)
        for element in nums:
            sum=sum+element
        for i in range(n):
            
            if sum1==sum-sum1-nums[i]:
                return i
            sum1+=nums[i]
        return -1