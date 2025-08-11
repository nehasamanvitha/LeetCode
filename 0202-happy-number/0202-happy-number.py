class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
       
        while n!=1 and n!=4:
            sum=0
            while n>0:
                
                x=n%10
                sum=sum+(x*x)
                n//=10
            n=sum
           
        if n==1:
            return True
        else:
            return False

        