class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
        if num<0:
            return '-'+self.convertToBase7(-num)
        rep=''
        while num>0:
            rep=str(num%7)+rep
            num=num//7
        return rep
