'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in (s[:i]+s[i+1:]):
                return i
        return -1
#######################################
class Solution(object):
    def firstUniqChar(self, s):
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
                
        for k in range(len(s)):
            if dicts[s[k]]==1:
                return k
        return -1
