class Solution:
    def isHappy(self, n: int) -> bool:
        return self.isHappyN(n,set())
    
    def  isHappyN(self,n,nset):
        if n==1:
            return True
        if n in nset:
            return False
        
        nset.add(n)
        rep=0
        while n>0:
            rep+=(n%10)**2
            n=n//10
        return self.isHappyN(rep,nset)
            
