class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        rep=[]
        self.getPartition(s,[],rep)
        return rep
    
    def getPartition(self,s,res,rep):
        if not s:
            rep.append(res)
            return
        for k in range(1,len(s)+1):
            if s[:k]==s[:k][::-1]:
                self.getPartition(s[k:],res+[s[:k]],rep)
    
