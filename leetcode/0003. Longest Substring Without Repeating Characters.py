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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<1:
            return 0
        i=0
        left=0
        max_substring=0
        while i<len(s):
            if s[i] not in s[left:i]:
                i+=1
            else:
                max_substring=max(max_substring,len(s[left:i]))
                left=self.calculateSubstring(s,s[i],left)+1
                i+=1
        return max(max_substring,len(s[left:]))
               
    def calculateSubstring(self,s,ss,left):
        for i in range(left,len(s)):
            if s[i]==ss:
                return i
