class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dict_t={}
        for t in time:
            if t%60 not in dict_t:
                dict_t[t%60]=1
            else:
                dict_t[t%60]+=1
        cnt=0
        if 0 in dict_t and dict_t[0]>1:
            cnt+=dict_t[0]*(dict_t[0]-1)//2
        if 30 in dict_t and dict_t[30]>1:
            cnt+=dict_t[30]*(dict_t[30]-1)//2
        for i in range(1,30):
            if i in dict_t and 60-i in dict_t:
                cnt+=dict_t[i]*dict_t[60-i]
        return cnt
