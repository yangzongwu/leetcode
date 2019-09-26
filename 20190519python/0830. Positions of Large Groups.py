class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if not S:
            return []
        rep=[]
        l,r=0,0
        while r<len(S):
            cnt=0
            while r<len(S) and S[r]==S[l]:
                cnt+=1
                r+=1
            if r==len(S):
                if cnt>=3:
                    rep.append([l,r-1])
                break
            if r>=l+3:
                rep.append([l,r-1])
            l=r
        return rep
