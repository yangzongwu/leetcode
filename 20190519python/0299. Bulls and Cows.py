class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cntA=0
        cntB=0
        dict_guess={}
        for k in range(len(secret)):
            if secret[k]==guess[k]:
                cntA+=1
        
        for s in secret:
            if s not in dict_guess:
                dict_guess[s]=1
            else:
                dict_guess[s]+=1
        for s in guess:
            if s in dict_guess and dict_guess[s]>0:
                cntB+=1
                dict_guess[s]-=1
        cntB-=cntA
        
        return str(cntA)+'A'+str(cntB)+'B'
