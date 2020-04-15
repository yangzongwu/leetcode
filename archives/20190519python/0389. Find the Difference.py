class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict={}
        for c in s:
            if c not in s_dict:
                s_dict[c]=1
            else:
                s_dict[c]+=1
        for c in t:
            if c not in s_dict or s_dict[c]==0:
                return c
            s_dict[c]-=1
