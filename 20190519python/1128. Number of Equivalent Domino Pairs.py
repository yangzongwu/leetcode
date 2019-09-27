class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        rep=0
        tmp=[0 for i in dominoes]
        for i in range(len(dominoes)-1):
            if tmp[i]!=0:
                continue
            cnt=0
            for j in range(i+1,len(dominoes)):
                if tmp[j]==0 and ((dominoes[i][0]==dominoes[j][0] and dominoes[i][1]==dominoes[j][1]) or (dominoes[i][0]==dominoes[j][1] and dominoes[i][1]==dominoes[j][0])):
                    tmp[j]=1
                    cnt+=1
            rep+=(cnt+1)*cnt//2
        return rep
