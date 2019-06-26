class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        S=S.lower()
        str_loc=[]
        res=[]
        for k in range(len(S)):
            res.append(S[k])
            if S[k] in "qwertyuiopasdfghjklzxcvbnm":
                str_loc.append(k)
       
        rep=[]
        self.get_letterCasePermutation(res,rep,str_loc) 
        return rep
    
    def get_letterCasePermutation(self,res,rep,str_loc):
        rep.append(''.join(res))
        
        for i in range(len(str_loc)):
            res[str_loc[i]]=res[str_loc[i]].upper()
            self.get_letterCasePermutation(res,rep,str_loc[i+1:])
            res[str_loc[i]]=res[str_loc[i]].lower()
        return 
