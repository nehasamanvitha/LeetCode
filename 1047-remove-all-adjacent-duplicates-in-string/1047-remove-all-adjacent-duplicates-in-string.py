class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for ch in s:
            if not stack:
                stack.append(ch)
            elif stack[-1]!=ch:
                stack.append(ch)
            else:
                stack.pop()
        return ''.join(stack)
        