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
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        dict_s={}
        for k in range(len(s)):
            if s[k] not in dict_s:
                dict_s[s[k]]=1
            else:
                dict_s[s[k]]+=1
        for k in range(len(s)):
            if dict_s[s[k]]==1:
                return k
        return -1
