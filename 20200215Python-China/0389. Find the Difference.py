'''
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict_s={}
        for ss in s:
            if ss not in dict_s:
                dict_s[ss]=1
            else:
                dict_s[ss]+=1
        
        for tt in t:
            if tt not in dict_s:
                return tt
            if dict_s[tt]==0:
                return tt
            dict_s[tt]-=1
