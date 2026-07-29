class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        for ch in tokens:
            
                if ch=='+':
                    if stack:
                        x=stack[-1]
                        y=stack[-2]
                        stack.pop()
                        stack.pop()
                        stack.append(y+x)
                elif ch=='-':
                    if stack:
                        x=stack[-1]
                        y=stack[-2]
                        stack.pop()
                        stack.pop()
                        stack.append(y-x)
                elif ch=='*':
                    if stack:
                        x=stack[-1]
                        y=stack[-2]
                        stack.pop()
                        stack.pop()
                        stack.append(y*x)
                elif ch == '/':
                    if stack:
                        x = stack[-1]
                        y = stack[-2]
                        stack.pop()
                        stack.pop()

                        if y * x < 0:
                          stack.append(-(abs(y) // abs(x)))
                        else:
                           stack.append(abs(y) // abs(x))
                else:
                    stack.append(int(ch))
        return stack[0]
            


        