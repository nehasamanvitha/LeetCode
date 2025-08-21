class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def quick_sort(arr):
            if len(arr)<=1:
                return arr
            pivot=arr[-1]
            left=[x for x in arr[:-1]if x>pivot]
            right=[x for x in arr[:-1]if x<=pivot]
            return quick_sort(left)+[pivot]+quick_sort(right)
        arr=quick_sort(nums)
        seen=set()
        count=0
        for i in arr:
            if i not in seen:
                count+=1
                seen.add(i)
                if count==3:
                    return i
        return arr[0]   
        
            
