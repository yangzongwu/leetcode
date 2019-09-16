class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        dict_N={}
        for i in range(1,N+1):
            dict_N[i]=0
        
        for tr in trust:
            dict_N[tr[0]]=-1
            if dict_N[tr[1]]!=-1:
                dict_N[tr[1]]+=1
                
        for k in dict_N:
            if dict_N[k]==N-1:
                return k
        return -1
