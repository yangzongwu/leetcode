class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        flag=1
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            flag=-1
        dividend,divisor=abs(dividend),abs(divisor)
        
        result=0
        while dividend>=divisor:
            rep=[1]
            res=[divisor]
            while res[-1]+res[-1]<dividend:
                res.append(res[-1]+res[-1])
                rep.append(rep[-1]+rep[-1])
            result+=rep[-1]
            dividend-=res[-1]
        
        if flag==-1:
            result=-result
            
        if result>2**31-1:
            return 2**31-1
        return result
