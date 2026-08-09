class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(index, current):
            if index == len(nums):
                result.append(current[:])
                return

            # Include the current element
            current.append(nums[index])
            backtrack(index + 1, current)

            # Remove it (backtrack)
            current.pop()

            # Don't include the current element
            backtrack(index + 1, current)

        backtrack(0, [])
        return result