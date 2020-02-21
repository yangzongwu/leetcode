'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict_s={}
        for ss in s:
            if ss not in dict_s:
                dict_s[ss]=1
            else:
                dict_s[ss]+=1
        
        rep=0
        flag=False
        for key in dict_s:
            if dict_s[key]%2==0:
                rep+=dict_s[key]
            else:
                flag=True
                rep+=dict_s[key]//2*2
        if flag==True:
            rep+=1
        
        return rep
