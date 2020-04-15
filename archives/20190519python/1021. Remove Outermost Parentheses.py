class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        flag=0
        rep=""
        k=0
        while k<len(S):
            if flag==0:
                flag+=1
                k+=1
            elif flag==1 and S[k]==")":
                flag-=1
                k+=1
            elif S[k]=="(":
                rep+=S[k]
                flag+=1
                k+=1
            elif S[k]==")":
                rep+=S[k]
                flag-=1
                k+=1
        return rep
        
