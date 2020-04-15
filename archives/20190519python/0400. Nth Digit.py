class Solution:
    def findNthDigit(self, n: int) -> int:
        digit=1
        while n>9*10**(digit-1)*digit:
            n-=9*10**(digit-1)*digit
            digit+=1
        
        num=10**(digit-1)+(n-1)//digit
        loc=(n-1)%digit
        
        return int(str(num)[loc])
        
