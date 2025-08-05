class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        x=""
        shortest=min(strs,key=len)
        for i in range(len(shortest)):
            char=shortest[i]
            if all(char==s[i] for s in strs):
                x+=char
            else:
                break
        return x