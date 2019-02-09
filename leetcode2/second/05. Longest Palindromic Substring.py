'''
遗漏边界条件，当s不存在或者为单个字符的情况
'''
class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        if not s:
            return ''
        if len(s)==1:
            return s
        i=0
        rep=''
        cnt=0
        for i in range(len(s)-1):
            tmp=self.subSingleLongestPalindrome(s,i)
            if tmp[0]>cnt:
                cnt=tmp[0]
                rep=tmp[1]
            if s[i]==s[i+1]:
                tmp=self.subDoubleLongestPalindrome(s,i)
                if tmp[0]>cnt:
                    cnt=tmp[0]
                    rep=tmp[1]
        return rep
    
    def subSingleLongestPalindrome(self,s,i):
        j=1
        while i-j>=0 and i+j<len(s) and s[i-j]==s[i+j]:
            j+=1
        j=j-1
        return 2*j+1,s[i-j:i+j+1]
    
    def subDoubleLongestPalindrome(self,s,i):
        j=1
        while i-j>=0 and i+1+j<len(s) and s[i-j]==s[i+1+j]:
            j+=1
        j=j-1
        return 2*j+2,s[i-j:i+1+j+1]
    
    
