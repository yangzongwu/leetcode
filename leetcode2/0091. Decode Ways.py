
class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        if not s:
            return 0
        if s[0]=='0':
            return 0
        dp=[1,1]
        for k in range(1,len(s)):
            cnt=0
            if 10<=int(s[k-1:k+1])<=26:
                cnt+=dp[-2]
            if s[k]!='0':
                cnt+=dp[-1]
            dp.append(cnt)
        return dp[-1]
            

##################################################################
class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        if not s:
            return 0
        elif s[0]=='0':
            return 0
        elif len(s)==1:
            return 1
        elif len(s)==2:
            if s[0] in '3456789':
                return self.numDecodings(s[1:])
            elif s[0]=='2' and s[1] in '7890':
                return 1
            elif s[1]=='0':
                return 1
            else:
                return 2
        else:
            if s[0] in '3456789':
                return self.numDecodings(s[1:])
            elif s[0]=='2' and s[1] in '789':
                return self.numDecodings(s[2:])
            elif s[1]=='0':
                return self.numDecodings(s[2:])
            else:
                return self.numDecodings(s[1:])+self.numDecodings(s[2:])
