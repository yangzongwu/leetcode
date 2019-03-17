class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dictt={}
        for t in time:
            s=t%60
            if s not in dictt:
                dictt[s]=1
            else:
                dictt[s]+=1
        rep=0
        if 0 in dictt:
            rep+=(dictt[0])*(dictt[0]-1)//2
        if 30 in dictt:
            rep+=(dictt[30])*(dictt[30]-1)//2
        for i in range(1,30):
            if (i in dictt) and (60-i in dictt):
                rep+=dictt[i]*dictt[60-i]
        return rep
