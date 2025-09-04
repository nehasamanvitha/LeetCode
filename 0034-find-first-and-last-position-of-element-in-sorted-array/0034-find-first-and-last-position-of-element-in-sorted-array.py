class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lowerbound(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
            return left
        def upperbound(nums,target):
            left,right=0,len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]<=target:
                    left=mid+1
                else:
                    right=mid-1
            return right
        left_index=lowerbound(nums,target)
        right_index=upperbound(nums,target)
        if left_index<=right_index:
            return [left_index,right_index]
        else:
            return [-1,-1]