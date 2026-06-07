class Solution(object):
    def generateValidStrings(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[str]
        """
        results = []
        
        def backtrack(current_str, current_cost, last_char, index):
            # Base Case: When the string reaches length n, check the cost limit
            if index == n:
                if current_cost <= k:
                    results.append(current_str)
                return
            
            # Decision 1: Append '0' 
            # (Always allowed; adds 0 to the total cost)
            backtrack(current_str + "0", current_cost, "0", index + 1)
            
            # Decision 2: Append '1' 
            # (Allowed only if the previous character was not '1')
            if last_char != "1":
                # The cost increases by the current 0-based index position
                backtrack(current_str + "1", current_cost + index, "1", index + 1)

        # Start the backtracking exploration from index 0
        backtrack("", 0, "", 0)
        
        return results