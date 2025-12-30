class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned=""
        for char in s:
            if 'A'<=char<='Z':
                cleaned+=chr(ord(char)+32)
            elif 'a'<=char<='z':
                cleaned+=char
            elif '0'<=char<='9':
                cleaned+=char
        left=0
        right=len(cleaned)-1
        while left<right:
            if cleaned[left]!=cleaned[right]:
                return False
            left+=1
            right-=1
        return True

            

            
        