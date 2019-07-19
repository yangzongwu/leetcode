class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        dp=[1,1]
        
        for k in range(1,len(s)):
            cnt=0
            if 10<=int(s[k-1:k+1])<=26:
                cnt+=dp[-2]
            if s[k]!='0':
                cnt+=dp[-1]
            dp.append(cnt)
        return dp[-1]
#====================================================
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        return self.getNumDecodings(s)
        
    def getNumDecodings(self,s):
        if not s:
            return 1
        if s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        if (s[0]=='1') or (s[0]=='2' and s[1] in '0123456'):
            return self.getNumDecodings(s[1:])+self.getNumDecodings(s[2:])
        else:
            return self.getNumDecodings(s[1:])
