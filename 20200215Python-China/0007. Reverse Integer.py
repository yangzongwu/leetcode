class Solution:
    def reverse(self, x: int) -> int:
        flag=True
        if x<0:
            flag=False
            x=-x

        rep=0
        while x>0:
            rep=rep*10+x%10
            x=(x-x%10)//10

        if flag==False:
            rep=-rep

        if rep>2**31-1 or rep<-2**31:
            return 0
        return rep
