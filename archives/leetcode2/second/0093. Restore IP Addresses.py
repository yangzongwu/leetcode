class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        self.rep=[]
        def dfs(s,res,n):
            if not s and n==0:
                self.rep.append('.'.join(res))
            if not s or len(s)>3*n:
                return
            for i in range(1,min(4,len(s)+1)):
                if i==1 or (int(s[:i])<=255 and s[0]!='0'):
                    dfs(s[i:],res+[s[:i]],n-1)
        
        
        dfs(s,[],4)
        return self.rep
