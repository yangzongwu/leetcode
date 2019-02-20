class Solution:
    def getHint(self, secret: 'str', guess: 'str') -> 'str':
        bulls,cows=0,0
        dicts={}
        cur=set()
        for k in range(len(secret)):
            if secret[k]==guess[k]:
                bulls+=1
                cur.add(k)
            else:
                if secret[k] not in dicts:
                    dicts[secret[k]]=[[k],1]
                else:
                    dicts[secret[k]][0].append(k)
                    dicts[secret[k]][1]+=1
        
        for k in range(len(guess)):
            if k not in cur:
                if guess[k] in dicts:
                    if dicts[guess[k]][1]>=1:
                        cows+=1
                        dicts[guess[k]][1]-=1
        return str(bulls)+'A'+str(cows)+'B'
