'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dicts={}
        for ss in s:
            if ss not in dicts:
                dicts[ss]=1
            else:
                dicts[ss]+=1
        for ss in t:
            if ss not in dicts:
                return False
            else:
                dicts[ss]-=1
        for ss in s:
            if dicts[ss]!=0:
                return False
        return True
