'''
Given two strings s and t , write a function to determine if t is an anagram of s.

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
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        dict_st={}
        for ss in s:
            if ss not in dict_st:
                dict_st[ss]=1
            else:
                dict_st[ss]+=1
        
        for tt in t:
            if tt not in dict_st or dict_st[tt]==0:
                return False
            dict_st[tt]-=1
        return True
