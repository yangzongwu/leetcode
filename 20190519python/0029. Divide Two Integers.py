class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor==1:
            return dividend
        if divisor==-1:
            dividend=-dividend
            if dividend>2**31-1 or dividend<-2**31:
                return 2**31-1
            else:
                return dividend
        flag=1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            flag=-1
        dividend,divisor=abs(dividend),abs(divisor)
        res=0
        while dividend>=divisor:
            cur=divisor
            rep=1
            while(cur<<1<dividend):
                cur<<=1
                rep<<=1
            res+=rep
            dividend-=cur
        
        if flag==-1:res=-res
        print(res)
        if res>2**31-1 or res<-2**31:
            return 2**31-1
        else:
            return res
        
