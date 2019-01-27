class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        l=0
        r=len(s)-1
        while l<len(s) and s[l] not in 'aoiueAOIUE':
            l+=1
        if l==len(s):
            return self.listtostr(s)
        while s[r] not in 'aoiueAOIUE':
            r-=1
        while r>=l+1:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
            while l<r and s[l] not in 'aoiueAOIUE':
                l+=1
            if l==r:
                return self.listtostr(s)
            while s[r] not in 'aoiueAOIUE':
                r-=1
        return self.listtostr(s)
    
    def listtostr(self,s):
        rep=''
        for ss in s:
            rep+=ss
        return rep
