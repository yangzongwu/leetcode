class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s='0ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rep=""
        while n>0:
            if n%26==0:
                rep='Z'+rep
                n=(n-(n-1)%26)//26
            else:
                rep=s[n%26]+rep
                n=(n-n%26)//26
        return rep    
                
                
        
                
