class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S=S.replace("-",'')
        if not S:
            return S
        S=S.upper()
        if len(S)<K:
            return S
        if len(S)%K==0:
            return self.subLicenseKeyFormatting(S,K)
        else:
            return S[:len(S)%K]+'-'+self.subLicenseKeyFormatting(S[len(S)%K:],K)
        
    def subLicenseKeyFormatting(self,S,K):
        if not S:
            return S
        rep=[]
        left=0
        while left+K<=len(S):
            rep.append(S[left:left+K])
            left+=K
        return '-'.join(rep)
