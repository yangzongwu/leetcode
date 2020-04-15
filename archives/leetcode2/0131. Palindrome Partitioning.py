class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        if not s:
            return []
        if len(s)==1:
            return [[s]]
        rep=[]
        for k in range(len(s)):
            tmp=[]
            if s[:k+1]==s[:k+1][::-1]:
                tmp.append([s[:k+1]])
            for i in range(1,k+1):
                if s[i:k+1]==s[i:k+1][::-1]:
                    for curlist in rep[i-1]:
                        tmp.append(curlist+[s[i:k+1]])
            rep.append(tmp)
        return rep[-1]
