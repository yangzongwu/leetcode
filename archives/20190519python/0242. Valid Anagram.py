class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict_st={}
        for ss in s:
            if ss in dict_st:
                dict_st[ss]+=1
            else:
                dict_st[ss]=1
        
        for tt in t:
            if tt in dict_st and dict_st[tt]>=1:
                dict_st[tt]-=1
            else:
                return False
        
        return True
