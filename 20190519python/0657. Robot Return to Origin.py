class Solution:
    def judgeCircle(self, moves: str) -> bool:
        target1=0
        target2=0
        for s in moves:
            if s=="U":target1+=1
            elif s=='D':target1-=1
            elif s=='L':target2+=1
            else:target2-=1
        return target1==0 and target2==0
                
