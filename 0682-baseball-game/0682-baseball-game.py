class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        for ch in operations:
            if ch=='C':
                stack.pop()
            elif ch=='D':
                stack.append(2*stack[-1])
            elif ch=='+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(ch))
        s=sum(stack)
        return s

        