class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if  not trust:
            if N==1:
                return 1
            else:
                return -1
        dictk={}
        rep=set()
        for num in trust:
            rep.add(num[0])
            if num[1] not in dictk:
                dictk[num[1]]=[num[0]]
            else:
                dictk[num[1]].append([num[0]])
        
        if len(rep)==N:
            return -1
        
        for key in dictk:
            if key not in rep:
                if len(dictk[key])==len(rep):
                    return key
        return -1
