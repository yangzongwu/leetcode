class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        rep='1'
        for _ in range(1,n):
            tmp=''
            left=0
            while left<len(rep):
                k=0
                while left+k<len(rep) and rep[left+k]==rep[left]:
                    k+=1
                tmp=tmp+str(k)+rep[left]
                left=left+k
            rep=tmp
        return rep
