class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)<=1:
            return False
        for k in range(1,len(s)//2+1):
            if len(s)%k==0 and s[:k]*(len(s)//k)==s:
                return True
        return False
    
