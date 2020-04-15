class Solution:
    def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':
        
        if numerator%denominator==0:
            return str(numerator//denominator)
        
        flag=''
        if numerator*denominator<0:
            flag='-'
        numerator,denominator=abs(numerator),abs(denominator)
        
        k=numerator//denominator
        numerator=numerator%denominator
        dictdenominator={}
        rep=''
        cnt=0
        while numerator!=0:
            if numerator not in dictdenominator:
                dictdenominator[numerator]=cnt
                cnt+=1
                rep+=str(numerator*10//denominator)
                numerator=numerator*10%denominator
            else:
                m=dictdenominator[numerator]
                if m==0:
                    rep='('+rep+')'
                else:
                    rep=rep[:m]+'('+rep[m:]+')'
                break
        return flag+str(k)+'.'+rep
