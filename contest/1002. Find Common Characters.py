class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        
        tmp=[]
        for num in A:
            dictnum={}
            for ss in num:
                if ss not in dictnum:
                    dictnum[ss]=1
                else:
                    dictnum[ss]+=1
            tmp.append(dictnum)
        
        rep=[]
        for s in 'qwertyuiopasdfghjklzxcvbnm':
            cnt=len(A[0])
            flag=True
            for dicts in tmp:
                if s not in dicts:
                    flag=False
                    continue
                else:
                    cnt=min(cnt,dicts[s])
            if flag==True:
                for _ in range(cnt):
                    rep.append(s)
        return rep
