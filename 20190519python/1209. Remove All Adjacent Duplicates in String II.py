class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        rep=[]
        for ss in s:
            if not rep:
                rep.append([ss,1])
            elif ss!=rep[-1][0]:
                rep.append([ss,1])
            else:
                if rep[-1][1]==k-1:
                    rep.pop()
                else:
                    rep[-1][1]+=1
        res=""
        for cur in rep:
            for k in range(cur[1]):
                res+=cur[0]
        return res
