class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Determine the valid search range for x based on abs(n - x) <= k
        lower_bound = max(1, n - k)
        upper_bound = n + k
        
        total_sum = 0
        
        # Iterate through all possible candidates for x
        for x in range(lower_bound, upper_bound + 1):
            # Check the bitwise condition: x and n must not share any set bits
            if (n & x) == 0:
                total_sum += x
                
        return total_sum