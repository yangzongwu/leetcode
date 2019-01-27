class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dictn={}
        for i in range(1,27):
            dictn[ss[i-1]]=i
        
        flag=1
        rep=0
        while s:
            rep=rep+dictn[s[-1]]*flag
            s=s[:-1]
            flag*=26
        return rep
        
