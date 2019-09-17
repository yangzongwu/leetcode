class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        cur=0
        for num in A:
            cur=cur*10+num
        cur+=K
        
        rep=[]
        for s in str(cur):
            rep.append(s)
        
        return rep
