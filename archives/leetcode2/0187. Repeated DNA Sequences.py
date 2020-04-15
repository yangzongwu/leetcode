class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dicts={}
        for k in range(len(s)-9):
            if s[k:k+10] not in dicts:
                dicts[s[k:k+10]]=1
            else:
                dicts[s[k:k+10]]+=1
        rep=[]
        for key in dicts:
            if dicts[key]>1:
                rep.append(key)
        return rep
