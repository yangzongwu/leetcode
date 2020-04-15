class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        if X>=Y:
            return X-Y
        else:
            rep=0
            while Y>X:
                if Y%2==0:
                    Y=Y//2
                    rep+=1
                else:
                    Y=(Y+1)//2
                    rep+=2
                    
            return rep+X-Y
