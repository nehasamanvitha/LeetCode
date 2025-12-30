class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        max_count=0
        result=None
        for x in nums:
            freq[x]=freq.get(x,0)+1
            if freq[x]>max_count:
                max_count=freq[x]
                result=x
        if (max_count>n//2):
            return result
        