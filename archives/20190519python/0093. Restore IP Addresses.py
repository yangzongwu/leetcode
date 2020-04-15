class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        rep=[]
        self.getIpAddresses(s,"",rep,4)
        return rep
    
    def getIpAddresses(self,s,res,rep,k):
        if k==0 and not s:
            rep.append(res[1:])
        if not s or (k==0 and s) or (len(s)>k*3):
            return
        
        for i in range(1,min(4,len(s)+1)):
            if int(s[:i])<=255 and (s[0]!='0' or (s[0]=='0' and len(s[:i])==1)):
                self.getIpAddresses(s[i:],res+'.'+s[:i],rep,k-1)
            
        
