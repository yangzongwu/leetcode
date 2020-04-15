class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num<0:
            return self.toHex(2**32+num)
        if num==0:
            return '0'
        cur=['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']        
        rep=''
        while num>0:
            if num%16:
                tmp=num%16
                num=num//16
                rep=cur[tmp-1]+rep
            else:
                tmp='0'
                num=num//16
                rep=tmp+rep
        return rep
