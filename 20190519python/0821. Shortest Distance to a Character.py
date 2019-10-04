class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        rep=[len(S)]*len(S)
        
        rep=self.getShortestToChar(S,C,rep)
        rep=self.getShortestToChar(S[::-1],C,rep[::-1])
        
        return rep[::-1]
    
    def getShortestToChar(Self,S,C,rep):
        k=0
        while k<len(S) and S[k]!=C:
            k+=1
            
        cur=k
        for i in range(k):
            rep[i]=min(rep[i],cur)
            cur-=1
        
        i=k
        while i<len(S):
            if S[i]==C:
                rep[i]=0
                i+=1
            else:
                tmp=1
                while i<len(S) and S[i]!=C:
                    rep[i]=min(rep[i],tmp)
                    i+=1
                    tmp+=1
        
        return rep
