class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        if not S:
            return []
        
        dicts={}
        for k in range(len(S)):
            dicts[S[k]]=k
                
        left=0
        cur=dicts[S[left]]
        rep=[]
        right=left
        while right<len(S):
            if right==cur:
                rep.append(right-left+1)
                right+=1
                left=right
                if right<len(S):
                    cur=dicts[S[right]]
                else:
                    break
            else:
                cur=max(cur,dicts[S[right]])
                right+=1
        if right>left:
            rep.append(right-left+1)
        return rep
                    
