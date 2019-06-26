class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        rep=[]
        self.get_combine(1,n,k,[],rep)
        return rep
    
    def get_combine(self,left,right,k,res,rep):
        if k==0:
            rep.append(res)
            return
        
        for i in range(left,right+1):
            self.get_combine(i+1,right,k-1,res+[i],rep)
            
        return
