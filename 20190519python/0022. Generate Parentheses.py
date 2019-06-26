class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        rep=set()
        self.get_generateParenthesis(n,0,"",rep)
        return list(rep)
    
    def get_generateParenthesis(self,n,flag,res,rep):
        if n==0 and flag==0:
            rep.add(res)
        elif n==0 and flag>0:
            self.get_generateParenthesis(n,flag-1,res+')',rep)
        elif n>0 and flag==0:
            self.get_generateParenthesis(n-1,flag+1,res+'(',rep)
        else:
            self.get_generateParenthesis(n-1,flag+1,res+'(',rep)
            self.get_generateParenthesis(n,flag-1,res+')',rep)
        return
