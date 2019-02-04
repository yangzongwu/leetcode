class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictstrs={}
        for ss in strs:
            s=''.join(sorted(ss))
            if s not in dictstrs:
                dictstrs[s]=[ss]
            else:
                dictstrs[s].append(ss)
        rep=[]
        for key in dictstrs:
            rep.append(dictstrs[key])
        return rep
