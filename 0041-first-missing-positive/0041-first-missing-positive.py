class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen={}
        for x in nums:
            if x>0:
                seen[x]=True
        i=1
        while True:
            if i not in seen:
                return i
            i+=1
        