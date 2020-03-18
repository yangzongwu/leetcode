'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rep=0
        cnt=0
        dict_s={}
        l,r=0,0
        while r<len(s):
            while r<len(s) and s[r] not in dict_s:
                dict_s[s[r]]=1
                r+=1
                cnt+=1
            rep=max(rep,cnt)
            if r<len(s):
                while s[r]!=s[l]:
                    del dict_s[s[l]]
                    cnt-=1
                    l+=1
                
                l+=1
                r+=1
                rep=max(rep,cnt)
        return rep
