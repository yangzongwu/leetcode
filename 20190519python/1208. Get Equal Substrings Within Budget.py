class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        rep=[]
        for k in range(len(s)):
            gap=self.getGapOfStr(s[k],t[k])
            rep.append(gap)
        
        res=0
        
        print(rep)
        
        l=0
        total=0
        r=0
        while l<len(rep):
            if r<len(rep) and total+rep[r]<=maxCost:
                while r<len(rep) and total+rep[r]<=maxCost:
                    total+=rep[r]
                    r+=1
                res=max(res,r-l)
            total-=rep[l]
            l+=1
        
        return res
        
        
        
    
    def getGapOfStr(self,str1,str2):
        strs='abcdefghijklmnopqrstuvwxyz'
        dict_s={}
        for k in range(len(strs)):
            dict_s[strs[k]]=k
        return abs(dict_s[str1]-dict_s[str2])
