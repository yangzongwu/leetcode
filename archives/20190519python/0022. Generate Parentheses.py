class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rep=[]
        self.get_generateParenthesis(n,0,"",rep)
        return rep
    
    def get_generateParenthesis(self,n,flag,res,rep):
        if n==0 and flag==0:
            rep.append(res)
        elif n==0 and flag>0:
            self.get_generateParenthesis(n,flag-1,res+')',rep)
        elif n>0 and flag==0:
            self.get_generateParenthesis(n-1,flag+1,res+'(',rep)
        else:
            self.get_generateParenthesis(n-1,flag+1,res+'(',rep)
            self.get_generateParenthesis(n,flag-1,res+')',rep)
        return
