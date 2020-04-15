class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts={}
        for ss in s:
            if ss not in dicts:
                dicts[ss]=1
            else:
                dicts[ss]+=1
        tmp1=0
        tmp2=0
        for key in dicts:
            tmp1+=dicts[key]//2*2
            tmp2+=dicts[key]%2
        if tmp2>0:
            tmp1+=1
        return tmp1
