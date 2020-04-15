class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rep=''
        if num>=1000:
            n=num//1000
            num=num%1000
            rep='M'*n
        if num>=900:
            num=num-900
            rep+='CM'
        if num>=500:
            num-=500
            rep+='D'
        if num>=400:
            num-=400
            rep+='CD'
        if num>=100:
            n=num//100
            num=num%100
            rep+='C'*n
        if num>=90:
            num=num-90
            rep+='XC'
        if num>=50:
            num-=50
            rep+='L'
        if num>=40:
            num-=40
            rep+='XL'
        if num>=10:
            n=num//10
            num=num%10
            rep+='X'*n
        if num>=9:
            num=num-9
            rep+='IX'
        if num>=5:
            num-=5
            rep+='V'
        if num>=4:
            num-=4
            rep+='IV'
        if num>=1:
            n=num//1
            num=num%1
            rep+='I'*n
        return rep
