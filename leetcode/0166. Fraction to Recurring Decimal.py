'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator*denominator>=0:
            return self.subfractionToDecimal(numerator, denominator)
        else:
            return '-'+self.subfractionToDecimal(abs(numerator), abs(denominator))
    def subfractionToDecimal(self, numerator, denominator):
        if numerator%denominator==0:
            return str(numerator//denominator)
        rep=[]
        tmp=[]
        left=numerator//denominator
        numerator=numerator%denominator
        while numerator !=0 and numerator not in tmp:
            tmp.append(numerator)
            rep.append(numerator*10//denominator)
            numerator=(numerator*10)%denominator
        result=str(left)+'.'
        if numerator==0:
            for i in rep:
                result=result+str(i)
        else:
            for k in range(len(tmp)):
                if numerator==tmp[k]:
                    break
            for i in rep[:k]:
                result=result+str(i)
            result+='('
            for i in rep[k:]:
                result=result+str(i)
            result+=')'
                    
        return result
