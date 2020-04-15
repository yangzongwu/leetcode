'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        elif len(s)==2:
            if s[0]=='1':return self.numDecodings(s[1:])+1
            elif s[0]=='2':
                if s[1] in '123456':
                    return 2
                else:return 1
            else:return self.numDecodings(s[1:])
        else:
            if s[0]=='1':
                return self.numDecodings(s[1:])+self.numDecodings(s[2:])
            elif s[0]=='2':
                if len(s)==1:
                    return 1
                elif s[1] in '0123456':
                    return self.numDecodings(s[1:])+self.numDecodings(s[2:])
                else:
                    return self.numDecodings(s[1:])
            else:
                return self.numDecodings(s[1:])
##############################################
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #k      0 1 2 
        # s=   '1 0 1'
        #rep=[1,1,1,]
        if not s or s[0]=='0':
            return 0
        rep=[1,1]
        for k in range(1,len(s)):
            tmp=0
            if 10<=int(s[k-1:k+1])<=26:
                tmp+=rep[k+1-2]
            if s[k]!='0':
                tmp+=rep[k+1-1]
            rep.append(tmp)
        return rep[-1]
        
