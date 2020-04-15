class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        cnt=1
        cur=A
        while len(cur)<len(B):
            cur+=A
            cnt+=1
        if B in cur:
            return cnt
        if B in cur+A:
            return cnt+1
        return -1
