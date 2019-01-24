class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if not strs[0]:
            return ''
        
        rep=0
        for k in range(len(strs[0])):
            for ss in strs[1:]:
                if k>=len(ss) or ss[k]!=strs[0][k]:
                    return strs[0][:k]
        return strs[0]
