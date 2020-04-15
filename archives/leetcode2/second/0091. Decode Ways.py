class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        dp=[1,1]
        for k in range(1,len(s)):
            if s[k]=='0':
                if s[k-1] in '34567890':
                    dp.append(0)
                else:
                    dp.append(dp[-2])
            else:
                if 9<int(s[k-1:k+1])<=26:
                    dp.append(dp[-1]+dp[-2])
                else:
                    dp.append(dp[-1])
            #print(dp)
        return dp[-1]
            
            
