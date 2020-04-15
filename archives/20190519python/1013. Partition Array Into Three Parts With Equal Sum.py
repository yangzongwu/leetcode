class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        A_sum=sum(A)
        if A_sum%3!=0:
            return False
        target=A_sum//3
        cur=0
        for i in range(len(A)):
            cur+=A[i]
            if cur==target:
                if self.canTwoPartsEqualSum(A[i+1:],target):
                    return True
        return False
    
    def canTwoPartsEqualSum(self,A,target):
        cur=0
        for i in range(len(A)):
            cur+=A[i]
            if cur==target:
                return True
        return False
