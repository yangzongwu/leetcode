class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        rep=[]
        
        def dfs(candidates,target,res,rep):
            if target==0:
                rep.append(res)
            if not candidates:
                return
            if target<0:
                return
            k=0
            while k<len(candidates):
                dfs(candidates[k+1:],target-candidates[k],res+[candidates[k]],rep)
                j=1
                while k+j<len(candidates) and candidates[k]==candidates[k+j]:
                    j+=1
                k+=j
        
        
        dfs(candidates,target,[],rep)
        return rep
        
