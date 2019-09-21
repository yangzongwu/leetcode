class Solution:
    def myPow(self, x: float, n: int) -> float:
        flag1=True
        if x<0:
            flag1=False
            x=-x
        
        if n<0:
            n=-n
            x=1/x
            
        cur=self.getMyPow(x,n)
        
        if flag1==False and n%2!=0:
            cur=-cur
        return cur
        
    def getMyPow(self,x,n):
        if n==0:
            return 1
        if n==1:
            return x
        if n%2==0:
            y=self.getMyPow(x,n//2)
            return y*y
        else:
            y=self.getMyPow(x,n//2)
            return y*y*x
