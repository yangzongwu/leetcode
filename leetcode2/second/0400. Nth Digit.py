class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        #  0-9   : 9
        #  10-99 : 90*2
        #  100-999: 900*3
        #  1000-9999: 9000*4
        
        if n<10:
            return n
        
        digit=1
        while n>9*(10**(digit-1))*digit:
            n-=9*(10**(digit-1))*digit
            digit+=1
            
        #n=11  12
        # ?10  11
        #   2   3   digit=2
        #  10+1
        tmp=int((n-1)//(digit)+10**(digit-1))
        loc=int((n-1)%(digit))
        return int(str(tmp)[loc])
