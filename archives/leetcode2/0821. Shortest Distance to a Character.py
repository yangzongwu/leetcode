class Solution:
    def shortestToChar(self, S: 'str', C: 'str') -> 'List[int]':
        dp1=self.subshortestToChar(S,C)
        dp2=self.subshortestToChar(S[::-1],C)[::-1]
        rep=[]
        for k in range(len(dp1)):
            rep.append(min(dp1[k],dp2[k]))
        return rep
    
    def subshortestToChar(self,S,C):
        rep=[]
        k=0
        while S[k]!=C:
            k+=1
            rep.append(k)
        rep=rep[::-1]
        
        cnt=0
        while k<len(S):
            if S[k]==C:
                rep.append(0)
                cnt=0
            else:
                cnt+=1
                rep.append(cnt)
            k+=1
        return rep
