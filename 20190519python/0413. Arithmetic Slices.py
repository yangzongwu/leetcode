class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        rep=[]
        for k in range(len(A)-1):
            rep.append(A[k+1]-A[k])
            
        res=0
        
        left,right=0,0
        while right<len(rep):
            while right<len(rep) and rep[right]==rep[left]:
                right+=1
                
            for i in range(1,right-left):
                res+=right-left-i
            
            left,right=right,right+1
        return res
