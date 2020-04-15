class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_p=len(p)
        len_s=len(s)
        if len_s<len_p:
            return []
        
        dicts={}
        for ss in s[:len_p]:
            if ss not in dicts:
                dicts[ss]=1
            else:
                dicts[ss]+=1
        dictp={}
        for pp in p:
            if pp not in dictp:
                dictp[pp]=1
            else:
                dictp[pp]+=1
                
        rep=[]
        if self.isSame(dicts,dictp):
            rep.append(0)
            
        for k in range(1,len_s-len_p+1):
            if dicts[s[k-1]]==1:
                dicts.pop(s[k-1])
            else:
                dicts[s[k-1]]-=1
                
            if s[k+len_p-1] in dicts:
                dicts[s[k+len_p-1]]+=1
            else:
                dicts[s[k+len_p-1]]=1
            
            if self.isSame(dicts,dictp):
                rep.append(k)
        
        return rep
    
    def isSame(self,dicts,dictp):
        for key in dicts:
            if key not in dictp or dicts[key]!=dictp[key]:
                return False
        return True
