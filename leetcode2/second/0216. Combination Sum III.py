class Solution:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        self.rep=[]
        def dfs(k,n,res,i):
            if k<0:
                return
            elif k==0:
                if res and n==0:
                    self.rep.append(res)
                return
            else:
                for j in range(i,10):
                    dfs(k-1,n-j,res+[j],j+1)
                return
        dfs(k,n,[],1)
        return self.rep
