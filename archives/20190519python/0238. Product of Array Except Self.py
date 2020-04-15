class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rep=[]
        cur=1
        for num in nums[::-1]:
            rep.append(cur)
            cur*=num
        rep=rep[::-1]
        
        tmp=[]
        cur=1
        for num in nums:
            tmp.append(cur)
            cur*=num
            
        for k in range(len(rep)):
            rep[k]=rep[k]*tmp[k]
            
        return rep
