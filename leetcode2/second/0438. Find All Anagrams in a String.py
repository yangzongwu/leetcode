class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
            return []
        dictp={}
        for pp in p:
            if pp not in dictp:
                dictp[pp]=1
            else:
                dictp[pp]+=1
        
        dicts={}
        for ss in s[:len(p)]:
            if ss not in dicts:
                dicts[ss]=1
            else:
                dicts[ss]+=1
        
        rep=[]
        if self.isSameDict(dicts,dictp):
            rep.append(0)
        len_p=len(p)
        
        for i in range(0,len(s)-len(p)):
            if dicts[s[i]]==1:
                dicts.pop(s[i])
            else:
                dicts[s[i]]-=1
            if s[i+len_p] not in dicts:
                dicts[s[i+len_p]]=1
            else:
                dicts[s[i+len_p]]+=1
            
            if self.isSameDict(dicts,dictp):
                rep.append(i+1)
        return rep
    
    def isSameDict(self,dicts,dictp):
        for key in dicts:
            if key not in dictp:
                return False
            if dicts[key]!=dictp[key]:
                return False
        return True
