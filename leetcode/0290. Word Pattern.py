'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''
class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        liststr=str.split()
        dictpattertostr={}
        
        if len(pattern)!=len(liststr):
            return False
        
        strlist=[]
        for k in range(len(pattern)):
            if pattern[k] not in dictpattertostr:
                if liststr[k] not in strlist:
                    dictpattertostr[pattern[k]]=liststr[k]
                    strlist.append(liststr[k])
                else:
                    return False
            else:
                if liststr[k]!=dictpattertostr[pattern[k]]:
                        return False
        return True
