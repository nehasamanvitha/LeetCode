class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        values={'I':1,'V':5,'X':10,'L':50,'C':100,
        'D':500,'M':1000}
        sum=0
        for i in range(n):
            if i<n-1 and values[s[i]]<values[s[i+1]]:
                sum-=values[s[i]]
            else:
                sum=sum+values[s[i]]

        return sum    
