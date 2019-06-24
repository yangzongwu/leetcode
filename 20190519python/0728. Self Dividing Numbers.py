class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        rep=[]
        for k in range(left,right+1):
            if self.isSelfDividingNumbers(k):
                rep.append(k)
        return rep
    
    def isSelfDividingNumbers(self,k):
        tmp=k
        while tmp>0:
            cur=tmp%10
            tmp=tmp//10
            if cur==0 or k%cur!=0:
                return False
        return True
