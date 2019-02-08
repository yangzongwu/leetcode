class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag=1
        if numerator*denominator<0:
            flag=-1
        numerator, denominator=abs(numerator),abs(denominator)
        if numerator%denominator==0:
            result=str(numerator//denominator)
            if flag==-1:
                return '-'+result
            else:
                return result
        left=numerator//denominator
        numerator=numerator%denominator
        rep1=[]
        rep2=[]
        while numerator!=0 and numerator not in rep1:
            rep1.append(numerator)
            rep2.append(numerator*10//denominator)
            numerator=numerator*10%denominator
        if numerator==0:
            res=''
            for s in rep2:
                res+=str(s)
            result=str(left)+'.'+res
        else:
            k=0
            while rep1[k]!=numerator:
                k+=1
            res=''
            for i in range(k):
                res+=str(rep2[i])
            res+='('
            for i in range(k,len(rep2)):
                res+=str(rep2[i])
            res=res+')'
            result=str(left)+'.'+res
        
        if flag==-1:
            return '-'+result
        else:
            return result
