class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        return self.getCountAndSay(n,"1")
    
    def getCountAndSay(self,n,strs):
        if n==1:
            return strs
        rep=""
        lo=0
        hi=0
        while hi<len(strs):
            while hi<len(strs) and strs[lo]==strs[hi]:
                hi+=1
            rep+=str(hi-lo)+strs[lo]
            lo=hi
        
        return self.getCountAndSay(n-1,rep)
