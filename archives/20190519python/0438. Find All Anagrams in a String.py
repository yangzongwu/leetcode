class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        rep=[]
        if len(p)>len(s):
            return rep
        
        dict_s={}
        for c in s[:len(p)]:
            if c not in dict_s:
                dict_s[c]=1
            else:
                dict_s[c]+=1
        
        dict_p={}
        for c in p:
            if c not in dict_p:
                dict_p[c]=1
            else:
                dict_p[c]+=1
        
        if self.isAnagrams(dict_s,dict_p):
            rep.append(0)
        
        for i in range(1,len(s)-len(p)+1):
            dict_s[s[i-1]]-=1
            if s[i+len(p)-1] not in dict_s:
                dict_s[s[i+len(p)-1]]=1
            else:
                dict_s[s[i+len(p)-1]]+=1
                
            if self.isAnagrams(dict_s,dict_p):
                rep.append(i)
        return rep
    
    
    
    def isAnagrams(self,dicts,dictp):
        for k in dictp:
            if k not in dicts or dicts[k]!=dictp[k]:
                return False
        return True
        
                
        
