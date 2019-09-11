class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur=[]
        cnt=1
        for k in range(1,len(s)):
            if s[k]==s[k-1]:
                cnt+=1
            else:
                cur.append(cnt)
                cnt=1
        cur.append(cnt)
        rep=0
        for k in range(1,len(cur)):
            rep+=min(cur[k],cur[k-1])
        return rep
            
