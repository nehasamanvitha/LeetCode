class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        x=max(a,b)
        count=0
        for i in range(1,x+1):
            if a%i==0 and b%i==0:
                count+=1
        return count
        