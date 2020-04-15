class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strlist=str.split(' ')
        if len(pattern)!=len(strlist):
            return False
        dictpattern={}
        strlistset=set()
        for k in range(len(pattern)):
            if pattern[k] not in dictpattern:
                if strlist[k] in strlistset:
                    return False
                else:
                    dictpattern[pattern[k]]=strlist[k]
                    strlistset.add(strlist[k])
            else:
                if dictpattern[pattern[k]]!=strlist[k]:
                    return False
        return True
