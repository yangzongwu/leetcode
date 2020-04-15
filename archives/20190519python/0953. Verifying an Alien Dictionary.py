class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        cnt=0
        dict_order={}
        for s in order:
            dict_order[s]=cnt
            cnt+=1
            
        for k in range(1,len(words)):
            if not self.cmpTwoString(words[k-1],words[k],dict_order):
                return False
        return True
    
    def cmpTwoString(self,str1,str2,dictcmp):
        for k in range(len(str1)):
            if k>=len(str2):
                return False
            if dictcmp[str1[k]]>dictcmp[str2[k]]:
                return False
            if dictcmp[str1[k]]<dictcmp[str2[k]]:
                return True
        return True
