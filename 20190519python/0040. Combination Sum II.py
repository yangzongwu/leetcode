class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        rep=[]
        self.getCombinationSum(candidates,[],rep,target)
        return rep
    
    def getCombinationSum(self,candidates,res,rep,target):
        if target==0:
            rep.append(res)
            return
        if not candidates or target<0:
            return
        k=0
        while k<len(candidates):
            tmp=candidates[k]
            self.getCombinationSum(candidates[k+1:],res+[tmp],rep,target-tmp)
            k+=1
            while k<len(candidates) and candidates[k]==tmp:
                k+=1
        
