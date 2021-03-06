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
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dictt={}
        for ss in t:
            if ss not in dictt:
                dictt[ss]=1
            else:
                dictt[ss]+=1
        for ss in s:
            dictt[ss]-=1
        for keys in dictt:
            if dictt[keys]==1:
                return keys
