class Solution:
    def frequencySort(self, s: 'str') -> 'str':
        dicts={}
        for ss in s:
            if ss not in dicts:
                dicts[ss]=1
            else:
                dicts[ss]+=1
        rep=[]
        for key in dicts:
            rep.append([key,dicts[key]])
            
        rep.sort(key=lambda x:x[1],reverse=True)
        
        res=''
        for s in rep:
            res+=s[0]*s[1]
        return res
