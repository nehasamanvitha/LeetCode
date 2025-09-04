class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=nums[0]
        y=0
        for i in range(len(nums)):
            if nums[i]>x:
                x=nums[i]
                y=i
        return y
       