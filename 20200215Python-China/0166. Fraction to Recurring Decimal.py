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
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator%denominator==0:
            return str(numerator//denominator)
        flag=''
        if numerator*denominator<0:
            flag='-'
        numerator=abs(numerator)
        denominator=abs(denominator)

        first_part=str(numerator//denominator)+'.'
        cur=numerator%denominator
        rep=[]
        second_part=''
        while cur not in rep:
            rep.append(cur)
            if 10*cur%denominator==0:
                return  flag+first_part+second_part+str(10*cur//denominator)
            second_part+=str(10*cur//denominator)
            cur=10*cur%denominator
        
        k=0
        while rep[k]!=cur:
            k+=1
        return flag+first_part+second_part[:k]+'('+second_part[k:]+')'
