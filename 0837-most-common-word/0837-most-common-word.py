class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        para1={}
        paragraph=paragraph.lower()
        for ch in "{}[]|:;""!?/.,'":
            paragraph=paragraph.replace(ch," ")
        paragraph=paragraph.split()
        for word in paragraph:
            if word not in para1:
                para1[word]=1
            else:
                para1[word]+=1
        temp=None
        max_freq=0
        for word in para1:
            if word not in banned and para1[word]>max_freq:
                max_freq=para1[word]
                temp=word
        return temp
        