class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==1:
            result=dividend
        elif divisor==-1:
            result=-dividend
        else:
            flag=1
            if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
                flag=-1
        
            dividend,divisor=abs(dividend),abs(divisor)
        
            result=0
            while dividend>=divisor:
                tmp=divisor
                rep=1
                while (tmp<<1)<=dividend:
                    tmp=tmp<<1
                    rep=rep<<1
                result+=rep
                dividend=dividend-tmp
                
            if flag==-1:
                result=-result
        if result>2**31-1:
            return 2**31-1
        elif result<-2**31:
            return -2**31
        else:
            return result
        
