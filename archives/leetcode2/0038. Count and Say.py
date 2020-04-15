class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        s='1'
        while n>1:
            rep=''
            cur=0
            while cur<len(s):
                k=0
                while cur+k <len(s) and s[cur+k]==s[cur]:
                    k+=1
                rep+=str(k)+s[cur]
                cur+=k
            s=rep
            n-=1
        return rep
