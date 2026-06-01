class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        avg_sum=sum(nums[:k])
        max_sum=avg_sum
        for i in range(k,len(nums)):
            avg_sum+=nums[i]-nums[i-k]
            max_sum=max(avg_sum,max_sum)

        return max_sum/float(k)

        