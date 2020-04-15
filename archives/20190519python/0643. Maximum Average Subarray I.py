class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res=sum(nums[:k])
        rep=res/k
        
        left=0
        for i in range(k,len(nums)):
            if nums[i]>nums[left]:
                res+=nums[i]-nums[left]
                rep=max(rep,res/k)
            else:
                res+=nums[i]-nums[left]
            left+=1
        return rep
