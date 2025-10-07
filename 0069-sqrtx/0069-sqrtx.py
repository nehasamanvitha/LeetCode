class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low,high=1,x
        
        ans=0
        if x==0 or x==1:
            return x
        while(low<=high):
            mid=(low+high)/2

            if mid*mid==x:

                return mid
            elif (mid*mid)<x:
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans
        