class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res=[]
        m=len(part)
        for ch in s:
            res.append(ch)
            if len(res)>=m and "".join(res[-m:])==part:
                del res[-m:]
        return "".join(res)
        