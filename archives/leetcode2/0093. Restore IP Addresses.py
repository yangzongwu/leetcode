class Solution:
    def restoreIpAddresses(self, s: 'str') -> 'List[str]':
        rep=[]
        self.subrestoreIpAddresses(s,'',rep,4)
        result=[]
        for s in rep:
            result.append(s[:-1])
        return result
    
    def subrestoreIpAddresses(self,s,res,rep,flag):
        if not s and flag==0:
            rep.append(res)
            return
        if not s:
            return
        for k in range(1,4):
            if k<=len(s) and int(s[:k])<=255 and ((len(s[:k])>1 and s[0]!='0') or len(s[:k])==1)  and flag-1<=len(s[k:])<=(flag-1)*3:
                self.subrestoreIpAddresses(s[k:],res+s[:k]+'.',rep,flag-1)
        
