class Solution:
    def intToRoman(self, num: int) -> str:
        rep=""
        while num>0:
            if num>=1000:
                rep+='M'
                num-=1000
            elif num>=900:
                rep+='CM'
                num-=900
            elif num>=500:
                rep+='D'
                num-=500
            elif num>=400:
                rep+='CD'
                num-=400
            elif num>=100:
                rep+='C'
                num-=100
            elif num>=90:
                rep+='XC'
                num-=90
            elif num>=50:
                rep+='L'
                num-=50
            elif num>=40:
                rep+='XL'
                num-=40
            elif num>=10:
                rep+='X'
                num-=10
            elif num>=9:
                rep+='IX'
                num-=9
            elif num>=5:
                rep+='V'
                num-=5
            elif num>=4:
                rep+='IV'
                num-=4
            elif num>=1:
                rep+='I'
                num-=1
        return rep
