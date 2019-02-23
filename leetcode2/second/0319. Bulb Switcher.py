class Solution:
    def bulbSwitch(self, n: 'int') -> 'int':
        rep=0
        for i in range(1,n+1):
            if i*i<=n:
                rep+=1
            else:
                break
        return rep
