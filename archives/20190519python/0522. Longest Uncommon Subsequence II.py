class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        if not strs:
            return 0
        if len(strs)==1:
            return len(strs[0])
        
        strs.sort()
        strs.sort(key=lambda x:len(x),reverse=True)
        
        for k in range(len(strs)):
            if k!=len(strs)-1:
                if self.strIsNotSubstring(strs[:k],strs[k]) and strs[k]!=strs[k+1]:
                    return len(strs[k])
            else:
                if self.strIsNotSubstring(strs[:k],strs[k]):
                    return len(strs[k])
        return -1
    
    def strIsNotSubstring(self,strs,str1):
        if not strs:
            return True
        for str2 in strs:
            if self.str1IsSubsequenceOfStr2(str1,str2):
                return False
        return True
    
    def str1IsSubsequenceOfStr2(self,str1,str2):
        k1,k2=0,0
        while k1<len(str1):
            while k1<len(str1) and k2<len(str2):
                if str1[k1]==str2[k2]:
                    k1+=1
                    k2+=1
                else:
                    k2+=1
            if k1==len(str1):
                return True
            return False
