class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S=S.replace('-','')
        S=S.upper()
        if not S:
            return ''
        firstpart=len(S)%K
        rep=[]
        if firstpart!=0:
            rep=[S[:firstpart]]+self.subsublicenseKeyFormatting(S[firstpart:],K)
        else:
            rep=rep+self.subsublicenseKeyFormatting(S,K)
        return '-'.join(rep)
    
    def subsublicenseKeyFormatting(self,S,K):
        if not S:
            return []
        rep=[]
        j=0
        while j<len(S):
            rep.append(S[j:j+K])
            j=j+K
        return rep
