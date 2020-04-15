class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag=1
        if x<0:
            flag=-1
            
        x=int(str(abs(x))[::-1])
        if flag==-1:x=-x
            
        if x>2**31-1 or x<-2**31:
            return 0
        else:
            return x
        
