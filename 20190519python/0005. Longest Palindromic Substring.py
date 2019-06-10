class Solution:
    def longestPalindrome(self, s: str) -> str:
        rep=""
        for i in range(len(s)):
            cur=self.getLongestPalindrome(s,i)
            if len(cur)>len(rep):
                rep=cur
        return rep
    
    def getLongestPalindrome(self,s,k):
        if k==0:
            if k+1<len(s) and s[k]==s[k+1]:
                return s[:2]
            else:
                return s[0]
        if k==len(s)-1:
            if k-1>=0 and s[k-1]==s[k]:
                return s[-2:]
            else:
                return s[-1]
        left,right=k-1,k+1
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        cur_str=s[left+1:right]
        
        if s[k]==s[k+1]:
            left,right=k-1,k+2
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
        cur_str2=s[left+1:right]
        
        return cur_str if len(cur_str)>len(cur_str2) else cur_str2
