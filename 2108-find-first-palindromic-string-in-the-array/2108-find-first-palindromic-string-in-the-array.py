class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for string in words:
            n=len(string)
            low=0
            high=n-1
            is_pal=True
            while (low<high):
                if string[low]!=string[high]:
                    is_pal=False
                    break
                    
                low+=1
                high-=1
            if is_pal:
                return string
        return ""
            
            
            

        