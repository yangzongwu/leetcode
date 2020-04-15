class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        rep=[]
        
        def dfs(left,n,k,res,rep):
            if k==0:
                rep.append(res)
                return
            if left<=n:
                for i in range(left,n+1):
                    dfs(i+1,n,k-1,res+[i],rep)
        
        dfs(1,n,k,[],rep)
        return rep
