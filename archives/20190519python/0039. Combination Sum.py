class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        rep=[]
        self.getCombinationSum(candidates,[],rep,target)
        return rep
    
    def getCombinationSum(self,candidates,res,rep,target):
        if not candidates or target<0:
            return
        if target==0:
            rep.append(res)
            return
        for k in range(len(candidates)):
            self.getCombinationSum(candidates[k:],res+[candidates[k]],rep,target-candidates[k])
        
