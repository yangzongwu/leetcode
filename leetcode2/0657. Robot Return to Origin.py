class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        cnt_U,cnt_L=0,0
        for s in moves:
            if s=='U':
                cnt_U+=1
            elif s=='D':
                cnt_U-=1
            elif s=='L':
                cnt_L+=1
            else:
                cnt_L-=1
        return cnt_U==0 and cnt_L==0
