class Solution:
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        bull=0
        cows=0
        dictbull={}
        for k in range(len(secret)):
            if secret[k]==guess[k]:
                bull+=1
            else:
                if secret[k] not in dictbull:
                    dictbull[secret[k]]=1
                else:
                    dictbull[secret[k]]+=1
        
        for k in range(len(guess)):
            if secret[k]!=guess[k]:
                if (guess[k] in dictbull) and dictbull[guess[k]]>0:
                    dictbull[guess[k]]-=1
                    cows+=1
        return str(bull)+'A'+str(cows)+'B'
        
