class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict={}
        for ch in s:
            if ch in s_dict:
                s_dict[ch]+=1
            else:
                s_dict[ch]=1
        t_dict={}
        for ch in t:
            if ch in t_dict:
                t_dict[ch]+=1
            else:
                t_dict[ch]=1
        if (s_dict==t_dict):
            return True
        else:
            return False

        
        