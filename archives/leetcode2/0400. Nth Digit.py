class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        #0-9       9
        #10-99     90*2+9
        #100-999   900*3+90*2+9
        #1000-9999 9000*4+900*3+90*2+9
        
        digit=1
        while n>9*10**(digit-1)*(digit):
            n-=9*10**(digit-1)*digit
            digit+=1
        
        #10 11 12 13  14
        #2  4  6   8  10
        
        #n=12  12-9=3 digit=2
        num=10**(digit-1)+(n-1)//digit   
        loc=(n-1)%digit
        
        return int(str(num)[loc])
        
        
        
