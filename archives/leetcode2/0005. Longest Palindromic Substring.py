class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=1:
            return s
        maxlen=0
        rep=''
        for k in range(len(s)-1):
            cur=self.single_longestPalindrome(s,k)[0]
            if cur>maxlen:
                maxlen=cur
                rep=self.single_longestPalindrome(s,k)[1]
            if s[k]==s[k+1]:
                cur=self.double_longestPalindrome(s,k)[0]
                if cur>maxlen:
                    maxlen=cur
                    rep=self.double_longestPalindrome(s,k)[1]
        return rep
    
    def single_longestPalindrome(self,s,k):
        cnt=0
        left,right=k-1,k+1
        while left>=0 and right<len(s) and s[left]==s[right]:
            cnt+=1
            left-=1
            right+=1
        return [2*cnt+1,s[k-cnt:k+cnt+1]]
    
    def double_longestPalindrome(self,s,k):
        cnt=0
        left,right=k-1,k+2
        while left>=0 and right<len(s) and s[left]==s[right]:
            cnt+=1
            left-=1
            right+=1
        return [2*cnt+2,s[k-cnt:k+cnt+2]]
