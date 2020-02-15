class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        rep=""
        cnt=0
        for ss in S:
            if cnt==0:
                cnt+=1
            else:
                if ss=="(":
                    rep+=ss
                    cnt+=1
                else:
                    if cnt==1:
                        cnt-=1
                    else:
                        cnt-=1
                        rep+=ss
        return rep
