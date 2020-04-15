class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rep=[]
        
        def dfs(candidates,target,res,rep):
            if target==0:
                rep.append(res)
            if not candidates:
                return
            if target<0:
                return
            for k in range(len(candidates)):
                dfs(candidates[k:],target-candidates[k],res+[candidates[k]],rep)
                
        
        
        dfs(candidates,target,[],rep)
        return rep
        
