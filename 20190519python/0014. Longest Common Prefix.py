class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len=len(strs[0])
        for s in strs:
            min_len=min(min_len,len(s))
            
        rep=0
        for i in range(min_len):
            target=strs[0][i]
            for s in strs[1:]:
                if s[i]!=target:
                    return strs[0][:rep]
            rep+=1
        return strs[0][:rep]
